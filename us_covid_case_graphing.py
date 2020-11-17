import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import mplcursors
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

def linegraph(x):
    # Create Dataframe
    df = pd.read_csv("C:\\Users\\Owner\\Documents\\covid_deaths_usafacts.csv", index_col=0)
    
    # Get list of states
    states = list(df.index.values)
    # Get list of dates
    dates = df.columns.tolist()
    
    fig = plt.figure(figsize=(100,350))
    ax = fig.add_subplot(2,1,1)
    
    plt.suptitle('Number of Cases by State', fontsize=14)
    
    # Iterate through states plotting lines on graph
    for state in states:
        for i in x:
            if i == state:
                row = df.loc[state, :]
                ax.plot(row.index, df.loc[state, :], label=state)
    
    ax.set_xticks(ax.get_xticks())
    ax.set_title('Source : https://usafacts.org/visualizations/coronavirus-covid-19-spread-map', fontsize='10')
    ax.set_xlabel('Date')
    ax.set_ylabel('# of Cases')
    ax.yaxis.get_ticklocs(minor=True)
    ax.minorticks_on()
    ax.xaxis.set_tick_params(which='minor', bottom=False)
    ax.grid(axis='y', which='both', linestyle='dotted', linewidth='0.5', color='black')
    handles,labels=ax.get_legend_handles_labels()
    ax.legend(list(handles), list(labels), loc='upper left', title='State',ncol=3, fontsize=6, handlelength=2)
    
    # Create Dataframe
    df2 = pd.read_csv("C:\\Users\\Owner\\Documents\\all-states-history.csv", index_col=0)
    
    # Get list of states
    states = list(df2.index.values)
    # Get list of dates
    dates = df2.columns.tolist()
    
    ax2 = fig.add_subplot(2,1,2)
    
    # Iterate through states plotting lines on graph
    for state in states:
        for i in x:
            if i == state:
                row = df2.loc[state, :]
                ax2.plot(row.index, df2.loc[state, :], label=state)
    
    ax2.set_xticks(ax2.get_xticks())
    ax2.set_title('Source :  https://covidtracking.com/data/download', fontsize='10')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('# of Cases')
    ax2.yaxis.get_ticklocs(minor=True)
    ax2.ticklabel_format(useOffset=False, style='plain', axis='y')
    ax2.minorticks_on()
    ax2.xaxis.set_tick_params(which='minor', bottom=False)
    ax2.grid(axis='y', which='both', linestyle='dotted', linewidth='0.5', color='black')
    handles,labels=ax2.get_legend_handles_labels()
    ax2.legend(list(handles), list(labels), loc='upper left', title='State',ncol=3, fontsize=6, handlelength=2)
    
    mplcursors.cursor(ax, hover=True)
    mplcursors.cursor(ax2, hover=True)
    
    plt.show()
    
def bargraph(x):
    # Create Dataframe
    df = pd.read_csv("C:\\Users\\Owner\\Documents\\covid_deaths_usafacts.csv", index_col=0)
        
    # Get list of states
    states = list(df.index.values)
    # Get list of dates
    dates = df.columns[::-1].tolist()
    
    fig = plt.figure(figsize=(100,350))
    ax = fig.add_subplot(2,1,1)
    
    plt.suptitle('Number of Cases by State', fontsize=14)
    
    # Iterate through dates plotting bars on graph (reverse order to stack bars)
    for date in dates:
        for i in x:
            if i == date:
                ax.bar(df.index, df[date], align='center', label=date)
        
    ax.set_xticks(ax.get_xticks())
    ax.set_xticklabels(df.index, rotation=90, ha='right', rotation_mode="anchor", fontsize='8')
    ax.set_title('Source : https://usafacts.org/visualizations/coronavirus-covid-19-spread-map', fontsize='10')
    ax.set_ylabel('# of Cases')
    ax.set_xlabel('State')
    ax.yaxis.get_ticklocs(minor=True)
    ax.minorticks_on()
    ax.xaxis.set_tick_params(which='minor', bottom=False)
    ax.grid(axis='y', which='both', linestyle='dotted', linewidth='0.5', color='black')
    handles,labels=ax.get_legend_handles_labels()
    ax.legend(list(reversed(handles)), list(reversed(labels)), loc='upper right', title='Date', fontsize=6, handlelength=2)
    
    # Create Dataframe
    df2 = pd.read_csv("C:\\Users\\Owner\\Documents\\all-states-history.csv", index_col=0)
    
    # Get list of states
    states = list(df2.index.values)
    # Get list of dates
    dates = df2.columns[::-1].tolist()
    
    ax2 = fig.add_subplot(2,1,2)
    
    # Iterate through dates plotting bars on graph (reverse order to stack bars)
    for date in dates:
        for i in x:
            if i == date:
                ax2.bar(df2.index, df2[date], align='center', label=date)
        
    ax2.set_xticks(ax2.get_xticks())
    ax2.set_xticklabels(df2.index, rotation=90, ha='right', rotation_mode="anchor", fontsize='8')
    ax2.set_title('Source :  https://covidtracking.com/data/download', fontsize='10')
    ax2.set_ylabel('# of Cases')
    ax2.set_xlabel('State')
    ax2.yaxis.get_ticklocs(minor=True)
    ax2.ticklabel_format(useOffset=False, style='plain', axis='y')
    ax2.minorticks_on()
    ax2.xaxis.set_tick_params(which='minor', bottom=False)
    ax2.grid(axis='y', which='both', linestyle='dotted', linewidth='0.5', color='black')
    handles,labels=ax2.get_legend_handles_labels()
    ax2.legend(list(reversed(handles)), list(reversed(labels)), loc='upper right', title='Date', fontsize=6, handlelength=2)
    
    mplcursors.cursor(ax, hover=True)
    mplcursors.cursor(ax2, hover=True)
    
    plt.show()
    
def threedgraph():
    # Create Dataframe
    df = pd.read_csv("C:\\Users\\Owner\\Documents\\covid_deaths_usafacts.csv", index_col=0)
        
    # Get list of states
    states = list(df.index.values)
    # Get list of dates
    dates = df.columns.tolist()
        
    dx, dy = .8, .8
    
    #fig = plt.figure(figsize=(10,6))
    fig = plt.figure(figsize=(30,20))
    #ax = Axes3D(fig)
    ax = fig.add_subplot(1,2,1, projection='3d')
    
    xpos=np.arange(df.shape[0])
    ypos=np.arange(df.shape[1])
    
    ax.set_xticks(xpos + dx/2)
    ax.set_yticks(ypos + dy/2)
    
    xpos, ypos = np.meshgrid(xpos, ypos)
    xpos = xpos.flatten()
    ypos = ypos.flatten()
    
    zpos=np.zeros(df.shape).flatten()
    
    dz=[]
    for date in dates:
        cases = df[date].tolist()
        dz = [*dz, *cases]
    
    ax.bar3d(xpos,ypos,zpos,dx,dy,dz,color='b')
    
    plt.suptitle('Number of Cases by State', fontsize=14)
    
    ax.set_title('Source : https://usafacts.org/visualizations/coronavirus-covid-19-spread-map', fontsize='10')
    ax.w_xaxis.set_ticklabels(df.index, rotation=45, ha='left', va='center', rotation_mode="anchor", fontsize='5') 
    ax.w_yaxis.set_ticklabels(df.columns, rotation=90, ha='right', rotation_mode="anchor", fontsize='6')
    zlab =['0','5000','10000','15000','20000','25000','30000']
    #ax.set_zticks(ax.get_zticks())
    ax.w_zaxis.set_ticklabels(zlab, fontsize='6')
    
    ax.set_xlabel('State')
    ax.set_ylabel('Date', labelpad=20)
    ax.set_zlabel('# of Cases')
    
    # Create Dataframe
    df2 = pd.read_csv("C:\\Users\\Owner\\Documents\\all-states-history.csv", index_col=0)
        
    # Get list of states
    states = list(df.index.values)
    # Get list of dates
    dates = df.columns.tolist()
    
    #fig2 = plt.figure(figsize=(30,20))
    ax2 = fig.add_subplot(1,2,2, projection='3d')
    
    xpos=np.arange(df2.shape[0])
    ypos=np.arange(df2.shape[1])
    
    ax2.set_xticks(xpos + dx/2)
    ax2.set_yticks(ypos + dy/2)
    
    xpos, ypos = np.meshgrid(xpos, ypos)
    xpos = xpos.flatten()
    ypos = ypos.flatten()
    
    zpos=np.zeros(df2.shape).flatten()
    
    dz=[]
    for date in dates:
        cases = df2[date].tolist()
        dz = [*dz, *cases]
    
    ax2.bar3d(xpos,ypos,zpos,dx,dy,dz,color='r')
    
    plt.suptitle('Number of Cases by State', fontsize=14)
    
    ax2.set_title('Source : https://covidtracking.com/data/download', fontsize='10')
    ax2.w_xaxis.set_ticklabels(df2.index, rotation=45, ha='left', va='center', rotation_mode="anchor", fontsize='5') 
    ax2.w_yaxis.set_ticklabels(df2.columns, rotation=90, ha='right', rotation_mode="anchor", fontsize='6')
    zlab =['0','5000','10000','15000','20000','25000','30000']
    #ax2.set_zticks(ax2.get_zticks())
    ax2.w_zaxis.set_ticklabels(zlab, fontsize='6')
    
    ax2.set_xlabel('State')
    ax2.set_ylabel('Date', labelpad=20)
    ax2.set_zlabel('# of Cases')
    
    plt.show()
    
def quit():
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
    statesLBx.selection_clear(0, END)
    datesLBx.selection_clear(0, END)
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

window = Tk()
window.title('COVID-19 Cases in the United States')
window.geometry('650x300')

img = ImageTk.PhotoImage(file='C:\\Users\\Owner\\Documents\\covid.jpg')
image = tk.Label(window, image=img).grid(row=1,column=1)

butOk = tk.Button(window,text='Graph',command=graph)
butOk.place(x=500,y=250)
butOk["state"] = 'disabled'

butQuit = tk.Button(window,text='Quit',command=quit)
butQuit.place(x=550,y=250)

stateLab = tk.Label(text='States', fg='black', font=('Arial', 10), width=10).grid(row=0,column=2)

states = tk.StringVar()
states.set(('AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'))
statesLBx = tk.Listbox(window, listvariable=states, exportselection=0, selectmode='multiple')
statesLBx.grid(row=1,column=2)
statesLBx.bind('<<ListboxSelect>>', on_select)

dateLab = tk.Label(text='Dates', fg='black', font=('Arial', 10), width=10).grid(row=0,column=3)

dates = tk.StringVar()
dates.set(('1/31/2020', '2/29/2020', '3/31/2020', '4/30/2020', '5/31/2020', '6/30/2020', '7/31/2020', '8/31/2020', '9/30/2020', '10/31/2020', '11/11/2020'))
datesLBx = tk.Listbox(window,listvariable=dates, exportselection=0, selectmode='multiple')
datesLBx.grid(row=1,column=3)
datesLBx.configure(state=DISABLED)
datesLBx.bind('<<ListboxSelect>>', on_select)

v = IntVar()
v.set(1)
lineRb = tk.Radiobutton(window,text='Line Graph',width=20,indicatoron=1,variable=v,value=1, command=updateGUI).grid(row=6,column=1)
barRb = tk.Radiobutton(window,text='Bar Graph',width=20,indicatoron=1,variable=v,value=2, command=updateGUI).grid(row=6,column=2)
threedRb = tk.Radiobutton(window,text='3D Graph',width=20,indicatoron=1,variable=v,value=3, command=updateGUI).grid(row=6,column=3)

window.mainloop()