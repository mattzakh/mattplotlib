import numpy as np
import matplotlib.pyplot as plt
# plt.style.use('../notebooks/test.mplstyle')
import seaborn as sns

from logs import logDecorator as lD 
import jsonref, pprint

config = jsonref.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.modules.test_plot.test_plot'


@lD.log(logBase + '.doSomething')
def doSomething(logger):
    '''print a line
    
    This function simply prints a single line
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    '''

    with plt.style.context('../notebooks/test.mplstyle'):

        w = 7.2
        fig = plt.figure(figsize=(w, w/1.6))  #, edgecolor='k', linewidth=2)
        ax = {}
        ax[0] = plt.axes([0.10, 0.10, 0.35, 0.30])
        ax[1] = plt.axes([0.55, 0.10, 0.35, 0.30])
        ax[2] = plt.axes([0.10, 0.57, 0.35, 0.30])
        ax[3] = plt.axes([0.55, 0.57, 0.35, 0.30])

        [ax[0].plot([1,2,3],np.random.randint([1,2,3],[10,9,8], size=3), marker='', label=f'line {i}') for i in range(4)]
        [ax[1].plot([1,2,3],np.random.randint([1,2,3],[10,9,8], size=3), linestyle='', label=f'marker {i}') for i in range(4)]

        params = ((10, 10), (4, 12), (50, 12), (6, 55))
        for a, b in params:
            values = np.random.beta(a, b, size=10000)
            ax[2].hist(values, histtype="stepfilled", bins=30,
                    alpha=0.2, density=True)

        mean, cov = [0, 2], [(1, .5), (.5, 1)]
        x, y = np.random.multivariate_normal(mean, cov, size=50).T
        # ax[3] = sns.kdeplot(x, linestyle='-', marker='', label='hist')#, marker='')

        fig.suptitle('Times New Roman')

        [ax[i].set_title(f'ax{i} Title') for i in range(4)]
        [ax[i].set_xlabel(f'ax{i} xlabel') for i in range(4)]
        [ax[i].set_ylabel(f'ax{i} ylabel') for i in range(4)]
        [ax[i].legend(loc='upper right') for i in range(4)]

        ax[3].set_xlabel(r'ax3 $a_i \sin(2\pi fx_i)$ label');

        plt.show

    plt.savefig('test.svg')

    return

@lD.log(logBase + '.main')
def main(logger, resultsDict):
    '''main function for module1
    
    This function finishes all the tasks for the
    main function. This is a way in which a 
    particular module is going to be executed. 
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    resultsDict: {dict}
        A dintionary containing information about the 
        command line arguments. These can be used for
        overwriting command line arguments as needed.
    '''


    doSomething()

    return

