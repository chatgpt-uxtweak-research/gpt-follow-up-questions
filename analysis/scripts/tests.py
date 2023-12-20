from scipy.stats import ttest_ind
from scipy.stats import mannwhitneyu
import pandas as pd, numpy as np
from scipy.stats import chi2_contingency
from scipy.stats import chisquare

def my_mannwhitney(data, columns, sample_column, sample_names):
    results = pd.DataFrame(columns=['Property', 'U', 'z', 'p', 'r', 'significant'])
    for column in columns:
        samples = [data[data[sample_column] == sample_name][column].dropna() for sample_name in sample_names]
        if(len(samples[0]) == 0 or len(samples[1]) == 0):
            continue
        stat, p = mannwhitneyu(*samples)
        nx = len(data[data[sample_column] == sample_names[0]][column])
        ny = len(data[data[sample_column] == sample_names[1]][column])
        z = (stat - nx*ny/2 + 0.5) / np.sqrt(nx*ny * (nx + ny + 1)/ 12)
        eff = z/np.sqrt(nx+ny)
        results.loc[len(results.index)] = [
            column, 
            np.round(stat, 2), 
            np.round(z, 2), 
            '< .001' if p <= 0.001 else str(np.round(p, 3)), 
            np.round(eff, 2), 
            p < 0.05
        ]
    return results

def my_mannwhitney_lite(sample1, sample2):
    result = pd.DataFrame(columns=['U', 'z', 'p', 'r', 'significant'])
    stat, p = mannwhitneyu(sample1, sample2)
    nx = len(sample1)
    ny = len(sample2)
    z = (stat - nx*ny/2 + 0.5) / np.sqrt(nx*ny * (nx + ny + 1)/ 12)
    eff = z/np.sqrt(nx+ny)
    result.loc[len(result.index)] = [
        np.round(stat, 2), 
        np.round(z, 2), 
        '< .001' if p <= 0.001 else str(np.round(p, 3)), 
        np.round(eff, 2), 
        p < 0.05
    ]
    return result


def my_ttest(data, columns, sample_column, sample_names):
    results = pd.DataFrame(columns=['Property', 't', 'p', 'df', 'd', 'significant'])
    for column in columns:
        samples = [data[data[sample_column] == sample_name][column].dropna() for sample_name in sample_names]
        if(len(samples[0]) == 0 or len(samples[1]) == 0):
            continue
        nx = len(data[data[sample_column] == sample_names[0]][column])
        ny = len(data[data[sample_column] == sample_names[1]][column])
        mx = np.mean(data[data[sample_column] == sample_names[0]][column])
        my = np.mean(data[data[sample_column] == sample_names[1]][column])
        vx = np.var(data[data[sample_column] == sample_names[0]][column])
        vy = np.var(data[data[sample_column] == sample_names[1]][column])
        res = ttest_ind(*samples)
        results.loc[len(results.index)] = [
            column, 
            np.round(res.statistic, 2), 
            '< .001' if res.pvalue <= 0.001 else str(np.round(res.pvalue, 3)),
            res.df, 
            np.round((mx - my) / ( np.sqrt( ( (nx-1) * vx ) + ( (ny-1) * vy ) / (nx+ny-2) ) ), 2),
            res.pvalue < 0.05
        ]
    return results

from statsmodels.sandbox.stats.multicomp import multipletests
from itertools import combinations

def my_chi(data):
    stat, p, d, exp = chi2_contingency(data)
    print("{low}pvalue: {p}\n".format(p=p, low='----> ' if p < 0.05 else ''))
    print("stat = {stat}, df = {df}".format(stat=stat, df=d))
    print("data")
    print(data)
    print('expected frequencies:')
    print(exp, end='\n\n')
    print("n=" + str(sum(sum(data,[]))))
    
    if(p < 0.05):
        p_vals = []

        for comb in list(combinations(data, 2)):
            _, p, _, _ = chi2_contingency(comb)
            p_vals.append(p)
        with np.errstate(divide='ignore'):
            reject_list, corrected_p_vals = multipletests(p_vals, method='fdr_gbs')[:2]

        print('Post-hoc testing:')
        combs = list(combinations(data, 2))
        for index, _ in enumerate(combs):
            print('{:40}{:20}{:20}'.format(str(combs[index]), corrected_p_vals[index], reject_list[index]))
        print('\n\n')