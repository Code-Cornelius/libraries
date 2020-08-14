# normal libraries
from abc import abstractmethod
import numpy as np  #maths library and arrays

# my libraries
from plot_functions import APlot
from classes.class_estimator import Estimator
from classes.graphs.class_graph_estimator import Graph_Estimator

np.random.seed(124)

# errors:


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Statistic_plot_estimator(Graph_Estimator):
    def __init__(self, estimator, separators=None):
        super().__init__(estimator = estimator, separators = separators)


    # section ######################################################################
    #  #############################################################################
    # data

    @abstractmethod
    def rescale_time_plot(self, rescale_factor, times):
        '''
        In order to plot not wrt time but wrt to a rescale factor.

        Args:
            rescale_factor:
            times:

        Returns:

        '''
        pass

    @abstractmethod
    def rescale_sum(self, sum, times):
        """Rescale the data, for instance the MSE. The method is useful bc I can rescale with attributes. Abstract method allows me to use specific scaling factor.
        I use it in order to normalize the sums.

        Args:
            sum:
            times:

        Returns:

        """
        pass

    # section ######################################################################
    #  #############################################################################
    # plot

    @abstractmethod
    def get_dict_fig(self, convergence_in):
        # convergence_in is simply a check parameter. It discriminates the dict_fig.
        pass



    def draw(self, mini_T, times, name_column_evolution, computation_function, class_for_hist, *args, separators=None, **kwargs):
        separators, global_dict, keys = super().draw(separators = separators)

        comp_sum = np.zeros(self.estimator.DF[name_column_evolution].nunique())
        for key in keys:
            data = global_dict.get_group(key)
            estimator = Estimator(data.copy())

            self.test_true_value(data) # test if there is only one true value i  the given sliced data. It could lead to potential big errors.
            estimator.function_upon_separated_data("value", computation_function, "computation",
                                                   true_parameter=estimator.DF["true value"].mean())

            comp_sum += estimator.DF.groupby([name_column_evolution])["computation"].sum()#.values

        TIMES_plot = self.rescale_time_plot(mini_T, times)
        comp_sum = self.rescale_sum(comp_sum, times).values

        plot = APlot()
        plot.uni_plot(0, TIMES_plot, comp_sum, dict_plot_param= {"linewidth" : 2})
        fig_dict = self.get_dict_fig(convergence_in ="MSE")
        plot.set_dict_fig(0, fig_dict)
        plot.save_plot(name_save_file=''.join([computation_function.__name__,'_comput']) )

        #I create a histogram:
        # first, find the DF with only the last estimation, which should always be the max value of column_evolution.
        max_value_evol = self.estimator.DF[name_column_evolution].max()

        #BIANCA class for estimator...
        hist_DF = self.estimator.__class__(self.estimator.DF[self.estimator.DF[name_column_evolution] == max_value_evol].copy())#copy() for independance

        # BIANCA how to get the class histogram Hawkes here?
        my_hist = class_for_hist(hist_DF, *args, **kwargs)
        my_hist.draw()
        return