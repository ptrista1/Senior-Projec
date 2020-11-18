#import required modules
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib._color_data as mcd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import mplcursors
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

# Path to files ***Please update path*** 
path = "C:\\Users\\Owner\\Documents\\"

# CSV files 
csv = path + "covid_deaths_usafacts.csv"
csv_ = path + "all-states-history_confirmed_deaths.csv"

# IMG file 
img = path + "covid.jpg"

def linegraph(x):
    # Create Dataframe
    df = pd.read_csv(csv, index_col=0)
    
    # Get list of states
    states = list(df.index.values)
    
    fig = plt.figure(figsize=(100,350))
    ax = fig.add_subplot(1,1,1)
    
    # Set title of plot
    plt.suptitle('Number of Deaths by State', fontsize=14)
    
    # Iterate through states plotting lines on graph
    for state in states:
        for i in x:
            if i == state:
                row = df.loc[state, :]
                cn = 'C' + str(x.index(i))
                ax.plot(row.index, df.loc[state, :], label=state, color=cn)
                
    # Create Dataframe
    df = pd.read_csv(csv_, index_col=0)
    
    # Get list of states
    states = list(df.index.values)
    
    # Iterate through states plotting lines on graph
    for state in states:
        for i in x:
            if i == state:
                row = df.loc[state, :]
                cn = 'C' + str(x.index(i))
                ax.plot(row.index, df.loc[state, :], label=state, color=cn, linestyle='dashed')
        
    # Set title for graph
    ax.set_title('Solid Line Source : https://usafacts.org/visualizations/coronavirus-covid-19-spread-map \nDashed Line Source : https://covidtracking.com/data/download', fontsize='10')
        
    # Configure x tick settings
    ax.set_xticks(ax.get_xticks())
    ax.set_xlabel('Date')
    ax.xaxis.set_tick_params(which='minor', bottom=False)
    
    # Configure y tick settings
    ax.set_ylabel('Deaths')
    ax.yaxis.get_ticklocs(minor=True)
    ax.grid(axis='y', which='both', linestyle='dotted', linewidth='0.5', color='black')
    
    ax.minorticks_on()
    
    # Configure legend
    handles,labels=ax.get_legend_handles_labels()
    ax.legend(list(handles), list(labels), loc='upper left', title='State',ncol=2, fontsize=6, handlelength=4)
    
    # Configure pop-ups on hover
    mplcursors.cursor(ax, hover=True)
    
    # Draw figure
    plt.show()
    
def bargraph(x):
    # Create Dataframe
    df = pd.read_csv(csv, index_col=0)
        
    # Get list of dates
    dates = df.columns[::-1].tolist()
    
    fig = plt.figure(figsize=(100,350))
    ax = fig.add_subplot(1,1,1)
    
    # Set title of plot
    plt.suptitle('Number of Deaths by State', fontsize=14)
    
    # Iterate through dates plotting bars on graph (reverse order to stack bars)
    for date in dates:
        for i in x:
            if i == date:
                cn = 'C' + str(x.index(i))
                ax.bar(df.index , df[date], width=-.45, align='edge', color=cn, edgecolor='black', label=date)
        
    # Create Dataframe
    df = pd.read_csv(csv_, index_col=0)
    
    # Get list of dates
    dates = df.columns[::-1].tolist()
    
    # Iterate through dates plotting bars on graph (reverse order to stack bars)
    for date in dates:
        for i in x:
            if i == date:
                cn = 'C' + str(x.index(i))
                ax.bar(df.index, df[date], width=.45, align='edge', color=cn, edgecolor='black', hatch='/', label=date)
    
    # Set title for graph
    ax.set_title('Solid Bar Source : https://usafacts.org/visualizations/coronavirus-covid-19-spread-map \nHatched Bar Source : https://covidtracking.com/data/download', fontsize='10')
    
    # Configure x tick settings
    ax.set_xticks(ax.get_xticks())
    ax.set_xticklabels(df.index, rotation=90, ha='right', rotation_mode="anchor", fontsize='8')
    ax.set_xlabel('State')
    
    # Configure y tick settings
    ax.set_ylabel('Deaths')
    ax.yaxis.get_ticklocs(minor=True)
    ax.ticklabel_format(useOffset=False, style='plain', axis='y')
    ax.grid(axis='y', which='both', linestyle='dotted', linewidth='0.5', color='black')
    
    ax.minorticks_on()
    ax.xaxis.set_tick_params(which='minor', bottom=False)
    
    # Configure legend
    handles,labels=ax.get_legend_handles_labels()
    ax.legend(list(reversed(handles)), list(reversed(labels)), ncol=2, loc='upper right', title='Date', fontsize=6, handlelength=4)
    
    # Configure pop-ups on hover
    mplcursors.cursor(ax, hover=True)
    
    # Draw figure
    plt.show()
    
def threedgraph():
    # Create Dataframe
    df = pd.read_csv(csv, index_col=0)
    
    # Get list of states
    states = list(df.index.values)
    
    # Get list of dates
    dates = df.columns.tolist()
    
    fig = plt.figure(figsize=(30,20))
    ax = fig.add_subplot(1,1,1, projection='3d')
    
    # Get bar heights
    dz=[]
    for date in dates:
        cases = df[date].tolist()
        dz = [*dz, *cases]
        
    # Set bar sizes
    dx, dy = .5, .5
    
    # Set x,y starting positions
    xpos=np.arange(df.shape[0])
    ypos=np.arange(df.shape[1])
    ax.set_xticks(xpos + dx/2)
    ax.set_yticks(ypos + dy/2)
    xpos, ypos = np.meshgrid(xpos, ypos)
    xpos = xpos.flatten()
    ypos = ypos.flatten()
    zpos=np.zeros(df.shape).flatten()
    
    # Plot 3D bars with settings for color and transparency
    ax.bar3d(xpos,ypos,zpos,dx,dy,dz,color='b',alpha=0.5)
    
    # Create Dataframe
    df = pd.read_csv(csv_, index_col=0)
    
    # Get list of states
    states2 = list(df.index.values)
        
    # Get list of dates
    dates = df.columns.tolist()
    
    # Get bar heights
    dz=[]
    for date in dates:
        cases = df[date].tolist()
        dz = [*dz, *cases]
    
    # Plot 3D bars with settings for color and transparency
    ax.bar3d(xpos,ypos,zpos,dx,dy,dz,color='r',alpha=0.5)
    
    # Set title of plot    
    ax.set_title('Blue Bar Source : https://usafacts.org/visualizations/coronavirus-covid-19-spread-map \nRed Bar Source : https://covidtracking.com/data/download', fontsize='10')
    
    # Configure x tick settings
    ax.w_xaxis.set_ticklabels(states, rotation=45, ha='left', va='center', rotation_mode="anchor", fontsize='5') 
    
    # Configure y tick settings
    ax.w_yaxis.set_ticklabels(dates, rotation=90, ha='right', rotation_mode="anchor", fontsize='6')
    
    # Configure z tick settings
    zlab =['0','5000','10000','15000','20000','25000','30000']
    #ax2.set_zticks(ax2.get_zticks()) #Supposed to resolve UserWarning: FixedFormatter should only be used together with FixedLocator but does not
    ax.w_zaxis.set_ticklabels(zlab, fontsize='6')
    
    # Configure tick labels
    ax.set_xlabel('State')
    ax.set_ylabel('Date', labelpad=20)
    ax.set_zlabel('Deaths')
    
    plt.show()
    
def quit():
    #Close window on quit
    window.destroy()
    
def graph():
    if (v.get() ==1):
        #call linegraph plot based on listbox selections
        sel_states_list = [statesLBx.get(i) for i in statesLBx.curselection()]
        linegraph(sel_states_list)
    elif (v.get() ==2):
        #call bargraph plot based on listbox selections
        sel_dates_list = [datesLBx.get(i) for i in datesLBx.curselection()]
        bargraph(sel_dates_list)
    else:
        #call 3dgraph plot based on listbox selections
        threedgraph()
        
def on_select(event):
    # Enable graph button if selection criteria is met
    if (v.get() ==1):
        if len(statesLBx.curselection()) > 0:
            sel_states_list = [statesLBx.get(i) for i in statesLBx.curselection()]
            butOk["state"] = 'normal'
        else:    
            butOk["state"] = 'disabled'
    elif (v.get() ==2):
        if len(datesLBx.curselection()) > 0:
            sel_dates_list = [datesLBx.get(i) for i in datesLBx.curselection()]
            butOk["state"] = 'normal'
        else:
            butOk["state"] = 'disabled'
    else:
        butOk["state"] = 'disabled'

def updateGUI():
    # Clear listbox selections
    statesLBx.selection_clear(0, END)
    datesLBx.selection_clear(0, END)
    
    # Update listbox status based on radio button selection
    if (v.get() ==1): 
        statesLBx.configure(state=NORMAL)
        datesLBx.configure(state=DISABLED)
        butOk["state"] = 'disabled'
    elif (v.get() ==2):
        datesLBx.configure(state=NORMAL)
        statesLBx.configure(state=DISABLED)
        butOk["state"] = 'disabled'
    else:
        datesLBx.configure(state=DISABLED)
        statesLBx.configure(state=DISABLED)
        butOk["state"] = 'normal'

# Create GUI window
window = Tk()
window.title('COVID-19 Cases in the United States')
window.geometry('650x300')

# Add image to GUI
img = ImageTk.PhotoImage(file=img)
image = tk.Label(window, image=img).grid(row=1,column=1)

# Configure graph button
butOk = tk.Button(window,text='Graph',command=graph)
butOk.place(x=500,y=250)
butOk["state"] = 'disabled'

# Configure quit button
butQuit = tk.Button(window,text='Quit',command=quit)
butQuit.place(x=550,y=250)

# Add label for state listbox
stateLab = tk.Label(text='States', fg='black', font=('Arial', 10), width=10).grid(row=0,column=2)

# Configure state listbox
states = tk.StringVar()
states.set(('AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'))
statesLBx = tk.Listbox(window, listvariable=states, exportselection=0, selectmode='multiple')
statesLBx.grid(row=1,column=2)
statesLBx.bind('<<ListboxSelect>>', on_select)

# Add label for date listbox
dateLab = tk.Label(text='Dates', fg='black', font=('Arial', 10), width=10).grid(row=0,column=3)

# Configure date listbox
dates = tk.StringVar()
dates.set(('1/31/2020', '2/29/2020', '3/31/2020', '4/30/2020', '5/31/2020', '6/30/2020', '7/31/2020', '8/31/2020', '9/30/2020', '10/31/2020', '11/11/2020'))
datesLBx = tk.Listbox(window,listvariable=dates, exportselection=0, selectmode='multiple')
datesLBx.grid(row=1,column=3)
datesLBx.configure(state=DISABLED)
datesLBx.bind('<<ListboxSelect>>', on_select)

# Configure radio buttons for graph type selection
v = IntVar()
v.set(1)
lineRb = tk.Radiobutton(window,text='Line Graph',width=20,indicatoron=1,variable=v,value=1, command=updateGUI).grid(row=6,column=1)
barRb = tk.Radiobutton(window,text='Bar Graph',width=20,indicatoron=1,variable=v,value=2, command=updateGUI).grid(row=6,column=2)
threedRb = tk.Radiobutton(window,text='3D Graph',width=20,indicatoron=1,variable=v,value=3, command=updateGUI).grid(row=6,column=3)

# Show window
window.mainloop()