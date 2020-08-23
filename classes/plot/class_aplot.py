# normal libraries
import functions.tools.classical_functions_dict
import numpy as np  # maths library and arrays
import seaborn as sns  # envrionement for plots
from errors.Error_forbidden import Error_forbidden
from matplotlib import pyplot as plt  # ploting
import warnings
import math  # quick math functions

sns.set()

# my libraries
from functions.tools import classical_functions
from metaclasses.metaclass_register import *

#errors:
from errors.Warning_deprecated import deprecated_function

# other files

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# plot graph can plot up to 2 graphs on the same figure.
# every argument has to be a list in order to make it work.
# title and labels has to be list, where one has :
## [title 1, title 2] ; [x1label y1label, x2label y2label]
# the set of parameters is the same for the two subplots.

### don't forget to write down #plt.show() at the end !
def plot_graph(data_x, data_y, title=["No title", "No title"], labels=["No label", "No label", "No label", "No label"],
               logy=[False, False], xint=[False, False], yint=[False, False],
               cum=[False, False], scater=[False, False],
               data2_x=None, data2_y=None,
               parameters=None, name_parameters=None,
               name_save_file=None):
    plt.figure(figsize=(10, 5))
    deprecated_function(reason="plot_graph. Use new version with class APlot.")

    markersize = 0.4
    if parameters is not None:
        nb_parameters = len(parameters)
        sous_text = " Parameters : \n"
        for i in range(nb_parameters):
            sous_text += str(name_parameters[i]) + f" = {parameters[i]}"
            # end of the list, we finish by a full stop.
            if i == nb_parameters - 1:
                sous_text += "."
            # certain chosen number of parameters by line, globally, 3 by line.
            # There shoudln't be more than 16 parameters
            elif i in [4, 7, 10, 13, 16]:
                sous_text += ", \n "
            # otherwise, just keep writing on the same line.
            else:
                sous_text += ", "
    if data2_x is not None:
        ax = plt.subplot(121)
        plt.grid(True)
        plt.xlabel(labels[0], fontsize=10)
        plt.ylabel(labels[1], fontsize=10)
        plt.title(title[0], fontsize=10)
        x = data_x
        y = data_y
        if scater[0]:
            plt.plot(x, y, 'mo', markersize=markersize, label=labels[1])
        else:
            plt.plot(x, y, 'mo-', markersize=markersize, linewidth=0.5, label=labels[1])
        if logy[0]:
            plt.xscale('log')
        # for cumulative, I use another axis on the right.
        if cum[0]:
            ax_bis = ax.twinx()
            ax_bis.plot(x, np.cumsum(y) / (np.cumsum(y)[-1]), color='darkorange',
                        marker='o', linestyle='-', markersize=1, label="Cumulative ratio")
            ax_bis.set_ylabel('cumulative ratio')
            ax_bis.set_ylim([0, 1.1])
            plt.legend(loc='best')
        # change ticks for every integers
        if xint[0]:
            x_int = range(min(x), math.ceil(max(x)) + 1)
            plt.xticks(x_int)
        if yint[0]:
            y_int = range(min(y), math.ceil(max(y)) + 2)
            plt.yticks(y_int)

        if parameters is not None:
            bottom, top = plt.ylim()
            left, right = plt.xlim()
            plt.text(left + (right - left) * 0.2, bottom - (top - bottom) * 0.43, sous_text, fontsize=10)
            plt.subplots_adjust(bottom=0.3, wspace=0.35)

        ax = plt.subplot(122)
        plt.grid(True)
        plt.xlabel(labels[2], fontsize=10)
        plt.ylabel(labels[3], fontsize=10)
        plt.title(title[1], fontsize=10)
        x = data2_x
        y = data2_y
        if scater[1]:
            plt.plot(x, y, 'mo', markersize=markersize, label=labels[1])
        else:
            plt.plot(x, y, 'mo-', linewidth=0.5, markersize=markersize, label=labels[1])
        if logy[1]:
            plt.xscale('log')
        # for cumulative, I use another axis on the right.
        if cum[1]:
            ax_bis = ax.twinx()
            ax_bis.plot(x, np.cumsum(y) / (np.cumsum(y)[-1]), color='darkorange',
                        marker='o', linestyle='-', markersize=1, label="Cumulative ratio")
            ax_bis.set_ylabel('cumulative ratio')
            ax_bis.set_ylim([0, 1.1])
            plt.legend(loc='best')
        # change ticks for every integers
        if xint[1]:
            x_int = range(min(x), math.ceil(max(x)) + 1)
            plt.xticks(x_int)
        if yint[1]:
            y_int = range(min(y), math.ceil(max(y)) + 2)
            plt.yticks(y_int)
        if name_save_file is not None:
            plt.savefig(name_save_file + '.png', dpi=1000)

    else:
        plt.grid(True)
        plt.xlabel(labels[0])
        plt.ylabel(labels[1])
        plt.title(title[0])
        x = data_x
        y = data_y
        if scater[0]:
            plt.plot(x, y, 'mo', markersize=markersize, label=labels[1])
        else:
            plt.plot(x, y, 'mo-', markersize=markersize, linewidth=0.5, label=labels[1])
        if logy[0]:
            plt.xscale('log')
        # for cumulative, I use another axis on the right.
        if cum[0]:
            ax = plt.subplot()
            ax_bis = ax.twinx()
            ax_bis.plot(x, np.cumsum(y) / (np.cumsum(y)[-1]), color='darkorange',
                        marker='o', linestyle='-', markersize=1, label="Cumulative ratio")
            ax_bis.set_ylabel('cumulative ratio')
            ax_bis.set_ylim([0, 1.1])
            plt.legend(loc='best')
        # change ticks for every integers
        if xint[0]:
            x_int = range(min(x), math.ceil(max(x)) + 1)
            plt.xticks(x_int)
        if yint[0]:
            y_int = range(min(y), math.ceil(max(y)) + 2)
            plt.yticks(y_int)

        if parameters is not None:
            bottom, top = plt.ylim()
            left, right = plt.xlim()
            plt.text(left + (right - left) * 0.2, bottom - (top - bottom) * 0.43, sous_text, fontsize=10)
            plt.subplots_adjust(bottom=0.3)
        if name_save_file is not None:
            plt.savefig(name_save_file + '.png', dpi=1000)
    return


# function for plotting histograms
def hist(data, bins, title, labels, range=None, total_number_of_simulations=None):
    deprecated_function(reason="hist. Use new version with class APlot.")
    plt.figure(figsize=(10, 5))
    ax = plt.axes()
    plt.ylabel("Nb of realisation inside a bin.")
    values, base, _ = plt.hist(data, bins=bins, density=False, alpha=0.5, color="green", range=range, label="Histogram")
    ax_bis = ax.twinx()
    values = np.append(values, 0)
    if total_number_of_simulations is not None:
        ax_bis.plot(base, np.cumsum(values) / total_number_of_simulations, color='darkorange', marker='o',
                    linestyle='-',
                    markersize=1, label="Cumulative Histogram")
    else:
        ax_bis.plot(base, np.cumsum(values) / np.cumsum(values)[-1], color='darkorange', marker='o', linestyle='-',
                    markersize=1, label="Cumulative Histogram")
    plt.xlabel(labels)
    plt.ylabel("Proportion of the cumulative total.")
    plt.title(title, fontsize=16, y=1.02)
    ax_bis.legend()
    ax.legend()
    return


# section ######################################################################
#  #############################################################################
# new plot functions


class APlot(metaclass=register):
    # TODO 23/08/2020 nie_k:  point plot for one point.
    # would be interesting to have objects like hist points lines ...
    # APlot is the class for my plots. APlot is one figure.

    default_dict_plot_param = {"color": 'm',
                               "linestyle": "solid",
                               "linewidth": 0.5,
                               "marker": "o",
                               "markersize": 0.4,
                               "label": "plot"
                               }

    @deco_register
    def __init__(self, how=(1, 1), datax=None, datay=None, figsize=(7, 5), sharex=False,
                 sharey=False):  # sharex,y for sharing the same on plots.
        # how should be a tuple with how I want to have axes.
        if datay is not None:
            if datax is not None:
                plt.figure(figsize=figsize)
                plt.plot(datax, datay, **APlot.default_dict_plot_param)
            else:
                plt.figure(figsize=figsize)
                plt.plot(range(len(datay)), datay, **APlot.default_dict_plot_param)

        else:  # corresponds to the case where we want to plot something
            # creation of the figu
            self.fig, self.axs = plt.subplots(*how, sharex=sharex, sharey=sharey, figsize=figsize)
            # true or false uni plot
            self.uni_dim = (how == (1, 1))
            # two cases, if it is uni_dim, I put self.axs into a list. Otherwise, it is already a list.
            # having a list is easier to deal with.
            if self.uni_dim:
                self.axs = [self.axs]
            else:
                # the axs are matrices, I need a list.
                self.axs = self.axs.flatten()
            # now, self.axs is always a list (uni dimensional).
            self.nb_of_axs = how[0] * how[1]  # nb of axes upon which I can plot


            # for the axs_bis, I store the axs inside this guy:
            self.axs_bis = [None] * self.nb_of_axs # a list full of zeros.

            # we set the default param of the fig:
            for i in range(self.nb_of_axs):
                self.set_dict_fig(i, None)

    def check_axs(self, ax):
        if ax < 0:
            warnings.warn("Axs given is negative. Lists are cyclic.")
        if ax >= self.nb_of_axs:
            warnings.warn("Axs given is out of bounds. I plot upon the first axis.")
            ax = 0
        return ax

    def set_dict_fig(self, nb_ax = 0, dict_fig = None, xx=None, yy=None):
        # always plotter first, then dict_updates (using the limits of the axis).
        # dict authorised:
        # {'title', 'xlabel', 'ylabel', 'xscale', 'xint', 'yint','parameters','name_parameters'}
        fontsize = 14.5
        nb_ax = self.check_axs(nb_ax)
        default_str = "Non-Defined."
        if dict_fig is None:
            dict_fig = {}
        default_dict = {'title': default_str, 'xlabel': default_str, 'ylabel': default_str,
                        'xscale': 'linear', 'xint': False, 'yint': False}
        functions.tools.classical_functions_dict.up(dict_fig, default_dict)

        self.axs[nb_ax].set_title(dict_fig['title'], fontsize=fontsize)
        self.axs[nb_ax].set_xlabel(dict_fig['xlabel'], fontsize=fontsize)
        self.axs[nb_ax].set_ylabel(dict_fig['ylabel'], fontsize=fontsize)
        self.axs[nb_ax].set_xscale(dict_fig['xscale'])
        self.axs[nb_ax].tick_params(labelsize=fontsize-1)


        if dict_fig['xint']:
            if xx is None:
                raise ("xx has not been given.")
            x_int = range(math.ceil(min(xx)) - 1, math.ceil(
                self.axs[nb_ax](
                    xx)) + 1)  # I need to use ceil on both if min and mself.axs[nb_ax] are not integers ( like 0 to 1 )
            self.axs[nb_ax].set_xticks(x_int)
        if dict_fig[('yint')]:
            if yy is None:
                raise ("yy has not been given.")
            y_int = range(min(yy), math.ceil(self.axs[nb_ax](yy)) + 1)
            self.axs[nb_ax].set_yticks(y_int)

        # I keep the condition. If not true, then no need to move the plot up.
        if 'parameters' in dict_fig and 'name_parameters' in dict_fig:
            #### check if this is correct
            # or fig ?
            parameters = dict_fig[('parameters')]
            name_parameters = dict_fig[('name_parameters')]
            nb_parameters = len(parameters)
            sous_text = " Parameters : \n"
            for i in range(nb_parameters):
                sous_text += str(name_parameters[i]) + f" = {parameters[i]}"
                # end of the list, we finish by a full stop.
                if i == nb_parameters - 1:
                    sous_text += "."
                # certain chosen number of parameters by line, globally, 3 by line.
                # There shoudln't be more than 16 parameters
                elif i in [4, 7, 10, 13, 16]:
                    sous_text += ", \n "
                # otherwise, just keep writing on the same line.
                else:
                    sous_text += ", "

            bottom, top = self.axs[nb_ax].get_ylim()
            left, right = self.axs[nb_ax].get_xlim()
            self.axs[nb_ax].text(left + (right - left) * 0.15, bottom - (top - bottom) * 0.42, sous_text,
                                 fontsize=fontsize - 1)
            plt.subplots_adjust(bottom=0.35, wspace=0.25, hspace=0.5)  # bottom is how much low;
            # the amount of width reserved for blank space between subplots
            # the amount of height reserved for white space between subplots

    def __my_plotter(self, nb_ax, xx, yy, dict_plot_param, bis = False):
        """
        A helper function to make a graph

        Parameters
        ----------
        nb_ax : Axes
            The axes to draw upon. Has to be an integer.

        xx : array
           The x data

        yy : array
           The y data

        dict_plot_param : dict
           Dictionary of kwargs to pass to ax.plot

        Returns
        -------
        out : list
            list of artists added
        """
        if len(xx) == len(yy):
            functions.tools.classical_functions_dict.up(dict_plot_param, APlot.default_dict_plot_param)
            nb_ax = self.check_axs(nb_ax)
            if not bis:  # bis is plot on second axis.
                out = self.axs[nb_ax].plot(xx, yy, **dict_plot_param)
                self.axs[nb_ax].grid(True)
            else:
                out = self.axs_bis[nb_ax].plot(xx, yy, **dict_plot_param)
                self.axs[nb_ax].grid(False)
                self.axs_bis[nb_ax].grid(False)
            return out
        else:
            Error_forbidden("Inputs plot not of matching size.")

    def uni_plot(self, nb_ax, xx, yy, dict_plot_param=default_dict_plot_param.copy(), dict_fig=None, tight=True):
        """
        Method to have 1 plot. Upon nb_ax (int)
        """
        self.__my_plotter(nb_ax, xx, yy, dict_plot_param)
        if tight:
            self.fig.tight_layout()
        if dict_fig is not None:
            self.set_dict_fig(nb_ax, dict_fig, xx, yy)


        return

    def uni_plot_ax_bis(self, nb_ax, xx, yy, dict_plot_param=default_dict_plot_param.copy(), dict_fig=None, tight = True):
        """ for now I add the ax bis to self.axs at the end. Access through -1.
        """

        #
        if self.axs_bis[nb_ax] is None:  # axis not created yet.
            self.axs_bis[nb_ax] = self.axs[nb_ax].twinx()  # instantiate a second axes that shares the same x-axis
        self.__my_plotter(nb_ax, xx, yy, dict_plot_param, bis=True)

        if tight:
            self.fig.tight_layout()

        if dict_fig is not None:
            self.set_dict_fig(nb_ax, dict_fig, xx, yy)
        return

    def bi_plot(self, nb_ax1, nb_ax2, xx1, yy1, xx2, yy2,
                dict_plot_param_1=default_dict_plot_param.copy(),
                dict_plot_param_2=default_dict_plot_param.copy(),
                dict_fig_1=None,
                dict_fig_2=None):
        self.uni_plot(nb_ax1, xx1, yy1, dict_plot_param=dict_plot_param_1, dict_fig=dict_fig_1)
        self.uni_plot(nb_ax2, xx2, yy2, dict_plot_param=dict_plot_param_2, dict_fig=dict_fig_2)
        return

    def plot_function(self, function, xx, nb_ax=0, dict_plot_param=default_dict_plot_param.copy()):
        # ax is an int, not necessary for uni dim case.
        yy = [function(x) for x in xx]
        self.__my_plotter(nb_ax, xx, yy, dict_plot_param)
        return

    def plot_line(self, a, b, xx, nb_ax=0, dict_plot_param=default_dict_plot_param.copy()):
        """
        Plot a line on the chosen ax.

        Args:
            a: slope of line
            b: origin of line
            xx: data, where to have the points of the line
            nb_ax: which ax to use, should be an integer.
            dict_plot_param:  if I want to customize the plot.

        Returns:

        """
        function = lambda x: a * x + b
        return self.plot_function(function, xx, nb_ax=nb_ax, dict_plot_param=dict_plot_param)

    def plot_vertical_line(self, x, yy, nb_ax=0, dict_plot_param=default_dict_plot_param.copy()):
        return self.uni_plot(nb_ax=nb_ax, xx=np.full(len(yy), x), yy=yy, dict_plot_param=dict_plot_param, tight = False)

    def cumulative_plot(self, xx, yy, nb_ax=0):
        """
        add cumulative plot of an nb_axis, for the chosen data set.

        Args:
            xx: xx where points should appear
            yy: the output data.
            nb_ax: which axis.

        Returns:

        """

        ax_bis = self.axs[nb_ax].twinx()
        ax_bis.plot(xx, np.cumsum(yy) / (np.cumsum(yy)[-1]), color='darkorange',
                    marker='o', linestyle='-', markersize=1, label="Cumulative ratio")
        ax_bis.set_ylabel('cumulative ratio')
        ax_bis.set_ylim([0, 1.1])
        self.axs[nb_ax].legend(loc='best')
        return

    default_dict_param_hist = {'bins': 20,
                               "color": 'green', 'range': None,
                               'label': "Histogram", "cumulative": True}

    def hist(self, data, nb_of_ax=0,
             dict_param_hist=default_dict_param_hist.copy(), # I need to copy because I am updating it. In particular I pop the cumulative.
             dict_fig=None):

        # function for plotting histograms
        if dict_fig is not None:
            self.set_dict_fig(nb_of_ax, dict_fig)
        self.axs[nb_of_ax].set_xlabel("Realisation")
        self.axs[nb_of_ax].set_ylabel("Nb of realisation inside a bin.")

        functions.tools.classical_functions_dict.up(dict_param_hist, APlot.default_dict_param_hist)

        try:
            # if doesn't pop, it will be catch by except.
            if dict_param_hist.pop("cumulative"):
                values, base, _ = self.axs[nb_of_ax].hist(data, density=False, alpha=0.5, **dict_param_hist)
                ax_bis = self.axs[nb_of_ax].twinx()
                values = np.append(values, 0)
                # I add 0 because I want to create the last line, which does not go up.
                # I put then 0 in order to have no evolution with cumsum.

                if 'total_number_of_simulations' in dict_param_hist:
                    ax_bis.plot(base, np.cumsum(values) / dict_param_hist[('total_number_of_simulations')],
                                color='darkorange', marker='o',
                                linestyle='-',
                                markersize=1, label="Cumulative Histogram")
                else:
                    ax_bis.plot(base, np.cumsum(values) / np.cumsum(values)[-1],
                                color='darkorange', marker='o', linestyle='-',
                                markersize=1, label="Cumulative Histogram")
                ax_bis.set_ylabel("Proportion of the cumulative total.")

        except KeyError:  # no cumulative in the hist.
            values, base, _ = self.axs[nb_of_ax].hist(data, density=False, alpha=0.5, **dict_param_hist)
        return

    def show_legend(self, nb_ax=None):
        # as usually, nb_ax is an integer.
        # if ax is none, then every nb_ax is showing the nb_ax.
        if nb_ax is None:
            for nb_ax_0 in range(self.nb_of_axs):
                self.axs[nb_ax_0].legend(loc='best', fontsize=12)
        else:
            self.axs[nb_ax].legend(loc='best', fontsize=12)
        return

    def save_plot(self, name_save_file='image'):
        """
        Method for saving the plot (figure) created.

        Args:
            name_save_file: name of the file

        Returns: nothing.
        """
        plt.savefig(name_save_file + '.png', dpi=800)
        return