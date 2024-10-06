# import external functions and python libraries 
import numpy as np
import pandas as pd
import webbrowser
from streamlit_option_menu import option_menu
import streamlit as st
import plotly_express as px
import os

#function to cleanse dataset
def cleanse():
    
    # data source
    url = "https://raw.githubusercontent.com/ISJ107Vee/my_dataset/refs/heads/main/dashboard_data.csv"

    # loading data into a dataframe
    factors_df = pd.read_csv(url)

    # removing duplicate rows
    factors_df.drop_duplicates(keep='first')

    # creating a list of the columns to remove
    columns = ['ID','Start time','Completion time','Email','Name','Last modified time']

    factors_df = factors_df.drop(columns, axis = 1) #dropping colums

    # proposed new column names list
    new_columns = [
        'Faculty','Registration Year','Funding','NSFAS Application Process',
        'Recommendations On NSFAS Process',
        'NSFAS Process Rating',
        'Residence','Reason for Off Campus Stay','Graduation Status','Completion Period',
        'Reason for No Graduation',
        'Major Challenges','Support','Challenges With Lecturers',
        'Lecture Ratings','Reason For Rating',
        'Employment Status','Employed In Field Of Study',
        'Period Spent Looking For Work','Was It Easy Applying Undergrad Knowledge',
        'Career Aspirations','TUT Rating','Recommendations'
    ]

    # renaming the columns in the dataframe
    factors_df = factors_df.set_axis(new_columns, axis = 1)

    #imputation on the columns with missing values
    columns = ['NSFAS Application Process','Recommendations On NSFAS Process']

    factors_df[columns] = factors_df[columns].fillna('Not Applicable')

    factors_df['NSFAS Process Rating'] = factors_df['NSFAS Process Rating'].fillna(0)

    columns = ['Reason for No Graduation', 'Employed In Field Of Study']

    factors_df[columns] = factors_df[columns].fillna('No Answer')

    factors_df['Reason for Off Campus Stay'] = factors_df['Reason for Off Campus Stay'].fillna('Not Applicable')

    # returning the cleansed dataframe
    return factors_df

# function to render star rating section
def render(rating_type, rating, total_entries, star_rating):
    
    # three colums to display the parameter of the function
    left_column, middle_column, right_column = st.columns(3)

    # TUT slogan on left column
    with left_column:
        st.subheader("TUT Slogan")
        st.subheader("We Empower People")
    
    # rating parameters
    with middle_column:
        st.subheader(rating_type)
        st.subheader(f"{rating} {star_rating}")
    
    # total number of respondents
    with right_column:
        st.subheader("Survey Entries")
        st.subheader(f"Entries: {total_entries}")
        
    st.markdown("---")

# function to plot two bar charts side by side
def plot(column1,title1,column2,title2,pos1,pos2,df = cleanse()):
    
    # setting up the first plot
    fig1 = px.bar(
        df[column1].value_counts(), 
        title=title1, 
        orientation = pos1
    )
    
    fig1.update_layout(
        plot_bgcolor = "rgba(0,0,0,0)",
        xaxis = (dict(showgrid=False))
    )
    
    # setting up the second plot
    fig2 = px.bar(
        df[column2].value_counts(), 
        title=title2, 
        orientation = pos2
    )

    fig2.update_layout(
        plot_bgcolor = "rgba(0,0,0,0)",
        xaxis = (dict(showgrid=False))
    )
    
    # plotting charts side by side
    left_column, right_column = st.columns(2)
    left_column.plotly_chart(fig1, use_container_width=True)
    right_column.plotly_chart(fig2, use_container_width=True)

factors_df = cleanse() # dataframe

# old faculties
faculties = list(factors_df['Faculty'].unique())

# Shortening faculty names
new_faculties = ['ICT','The Arts','EBE','Humanities','Ecos & Finance','Management Sci','Science']

factors_df['Faculty'] = factors_df['Faculty'].replace(faculties,new_faculties)

def faculty():

    selected = option_menu(
        menu_title = None,
        options = list(factors_df['Faculty'].unique()),
        menu_icon = 'cast',
        default_index = 0,
        orientation = 'horizontal'
    )

    if selected == 'ICT':

        # filtering by faculty
        Faculty_df = factors_df[factors_df['Faculty'] == 'ICT']

        rating_type = 'Lecturer Rating' # lecture rating
        
        # rating value
        rating = int(round(Faculty_df['Lecture Ratings'].mean(),0))

        star_rating = ":star:"*rating # getting star rating

        total_entries =  Faculty_df.shape[0] # getting number of respondents

        # setting up the main page
        render(rating_type, rating, total_entries, star_rating)

        plot(
            
            'Registration Year','Student Registrations By Year','Graduation Status',
            'Stundent Graduation Stats','v','h', df=Faculty_df
        )

        plot(
            
            'Completion Period','Graduation On Record Time','Challenges With Lecturers',
            'Challenges With Lecturers','h','v', df=Faculty_df
        )

        plot(
            
            'Lecture Ratings','Faculty Lecturer Rating','Reason For Rating',
            'Reason For Faculty Lecturer Rating','h','v', df=Faculty_df
        )
    
    elif selected == 'The Arts':

        # filtering by faculty
        Faculty_df = factors_df[factors_df['Faculty'] == 'The Arts']

        rating_type = 'Lecturer Rating' # lecture rating
        
        # rating value
        rating = int(round(Faculty_df['Lecture Ratings'].mean(),0))

        star_rating = ":star:"*rating # getting star rating

        total_entries =  Faculty_df.shape[0] # getting number of respondents

        # setting up the main page
        render(rating_type, rating, total_entries, star_rating)

        plot(
            
            'Registration Year','Student Registrations By Year','Graduation Status',
            'Stundent Graduation Stats','v','h', df=Faculty_df
        )

        plot(
            
            'Completion Period','Graduation On Record Time','Challenges With Lecturers',
            'Challenges With Lecturers','h','v', df=Faculty_df
        )

        plot(
            
            'Lecture Ratings','Faculty Lecturer Rating','Reason For Rating',
            'Reason For Faculty Lecturer Rating','h','v', df=Faculty_df
        )
    
    elif selected == 'EBE':
        
        # filtering by faculty
        Faculty_df = factors_df[factors_df['Faculty'] == 'EBE']

        rating_type = 'Lecturer Rating' # lecture rating
        
        # rating value
        rating = int(round(Faculty_df['Lecture Ratings'].mean(),0))

        star_rating = ":star:"*rating # getting star rating

        total_entries =  Faculty_df.shape[0] # getting number of respondents

        # setting up the main page
        render(rating_type, rating, total_entries, star_rating)

        plot(
            
            'Registration Year','Student Registrations By Year','Graduation Status',
            'Stundent Graduation Stats','v','h', df=Faculty_df
        )

        plot(
            
            'Completion Period','Graduation On Record Time','Challenges With Lecturers',
            'Challenges With Lecturers','h','v', df=Faculty_df
        )

        plot(
            
            'Lecture Ratings','Faculty Lecturer Rating','Reason For Rating',
            'Reason For Faculty Lecturer Rating','h','v', df=Faculty_df
        )
    
    elif selected == 'Humanities':

        # filtering by faculty
        Faculty_df = factors_df[factors_df['Faculty'] == 'Humanities']

        rating_type = 'Lecturer Rating' # lecture rating
        
        # rating value
        rating = int(round(Faculty_df['Lecture Ratings'].mean(),0))

        star_rating = ":star:"*rating # getting star rating

        total_entries =  Faculty_df.shape[0] # getting number of respondents

        # setting up the main page
        render(rating_type, rating, total_entries, star_rating)

        plot(
            
            'Registration Year','Student Registrations By Year','Graduation Status',
            'Stundent Graduation Stats','v','h', df=Faculty_df
        )

        plot(
            
            'Completion Period','Graduation On Record Time','Challenges With Lecturers',
            'Challenges With Lecturers','h','v', df=Faculty_df
        )

        plot(
            
            'Lecture Ratings','Faculty Lecturer Rating','Reason For Rating',
            'Reason For Faculty Lecturer Rating','h','v', df=Faculty_df
        )
    
    elif selected == 'Ecos & Finance':

        # filtering by faculty
        Faculty_df = factors_df[factors_df['Faculty'] == 'Ecos & Finance']

        rating_type = 'Lecturer Rating' # lecture rating
        
        # rating value
        rating = int(round(Faculty_df['Lecture Ratings'].mean(),0))

        star_rating = ":star:"*rating # getting star rating

        total_entries =  Faculty_df.shape[0] # getting number of respondents

        # setting up the main page
        render(rating_type, rating, total_entries, star_rating)

        plot(
            
            'Registration Year','Student Registrations By Year','Graduation Status',
            'Stundent Graduation Stats','v','h', df=Faculty_df
        )

        plot(
            
            'Completion Period','Graduation On Record Time','Challenges With Lecturers',
            'Challenges With Lecturers','h','v', df=Faculty_df
        )

        plot(
            
            'Lecture Ratings','Faculty Lecturer Rating','Reason For Rating',
            'Reason For Faculty Lecturer Rating','h','v', df=Faculty_df
        )
    
    elif selected == 'Management Sci':

        # filtering by faculty
        Faculty_df = factors_df[factors_df['Faculty'] == 'Management Sci']

        rating_type = 'Lecturer Rating' # lecture rating
        
        # rating value
        rating = int(round(Faculty_df['Lecture Ratings'].mean(),0))

        star_rating = ":star:"*rating # getting star rating

        total_entries =  Faculty_df.shape[0] # getting number of respondents

        # setting up the main page
        render(rating_type, rating, total_entries, star_rating)

        plot(
            
            'Registration Year','Student Registrations By Year','Graduation Status',
            'Stundent Graduation Stats','v','h', df=Faculty_df
        )

        plot(
            
            'Completion Period','Graduation On Record Time','Challenges With Lecturers',
            'Challenges With Lecturers','h','v', df=Faculty_df
        )

        plot(
            
            'Lecture Ratings','Faculty Lecturer Rating','Reason For Rating',
            'Reason For Faculty Lecturer Rating','h','v', df=Faculty_df
        )
    
    elif selected == 'Science':

        # filtering by faculty
        Faculty_df = factors_df[factors_df['Faculty'] == 'Science']

        rating_type = 'Lecturer Rating' # lecture rating
        
        # rating value
        rating = int(round(Faculty_df['Lecture Ratings'].mean(),0))

        star_rating = ":star:"*rating # getting star rating

        total_entries =  Faculty_df.shape[0] # getting number of respondents

        # setting up the main page
        render(rating_type, rating, total_entries, star_rating)

        plot(
            
            'Registration Year','Student Registrations By Year','Graduation Status',
            'Stundent Graduation Stats','v','h', df=Faculty_df
        )

        plot(
            
            'Completion Period','Graduation On Record Time','Challenges With Lecturers',
            'Challenges With Lecturers','h','v', df=Faculty_df
        )

        plot(
            
            'Lecture Ratings','Faculty Lecturer Rating','Reason For Rating',
            'Reason For Faculty Lecturer Rating','h','v', df=Faculty_df
        )
    
    else:

        pass

# setting up the page
st.set_page_config(page_title="TUT Feedback Dashboard",
                   page_icon=":bar_chart",
                   layout="wide"
)

#--------------------------Sidebar----------------------------------

# creating side bar menu
with st.sidebar:

    # creating selection options with radio buttons
    selected = option_menu(

        menu_title = "Dashboard Menu",
        options = ['Home', 'Faculty', 'Support', 'Career Outcomes','Logout'],
        menu_icon = "cast",
        default_index = 0,
    )

    st.image("TUT-Logo1.jpg")


#-------------------------Main Page-----------------------------------

st.title(":bar_chart: TUT Student Feedback Dashboard")
st.markdown("##")

rating_type = "TUT Rating"

# Tut average rating
rating = int(round(factors_df['TUT Rating'].mean(),0))

# tut average rating in stars
star_rating = ":star:"*rating

# number of total respondents
total_entries = factors_df.shape[0]

# creating options for pages based on selected options
if selected == "Home":

    # setting up the main page
    render(rating_type, rating, total_entries, star_rating)    

    plot(
        
        'TUT Rating','TUT Rating Distribution','Lecture Ratings',
        'Lecture Rating Distribution','h','v'
    )

    plot(

        'Challenges With Lecturers','Challenges With Lecturers',
        'Recommendations','Respondents Recommendations','h','h'
    )

elif selected == "Faculty":

    faculty()

elif selected == "Support":

    # NSFAS Rating
    NSFAS_Rating = factors_df[factors_df['NSFAS Process Rating'] != 0]['NSFAS Process Rating'].mean()

    NSFAS_Rating = int(round(NSFAS_Rating,0))

    star_rating = ":star:"*NSFAS_Rating

    # NSFAS Funded Students
    NSFAS_Count = factors_df[factors_df['NSFAS Process Rating'] != 0]['NSFAS Process Rating'].count()

    render("NSFAS Process Rating", NSFAS_Rating, NSFAS_Count, star_rating)

    plot(

        'Support','Support Outside Lectures','Funding',
        'Student Funding Distribution','v','h'
    )

    plot(

        'Residence','Student Residence Distribution',
        'Reason for Off Campus Stay','Reason for Off Campus Stay','v','h'
    )

    plot(

        'NSFAS Application Process','NSFAS Application Process Challenges',
        'Recommendations On NSFAS Process',
        'Recommendations On NSFAS Application Process','v','h'
    )

elif selected == "Career Outcomes":

    # setting up the main page
    render(rating_type, rating, total_entries, star_rating)

    plot(

        'Employment Status','Are You Currently Employed',
        'Employed In Field Of Study','Employed In Field Of Study','v','h'
    )

    plot(

        'Period Spent Looking For Work','Period Spent Looking For Work',
        'Was It Easy Applying Undergrad Knowledge','Was It Easy Applying Undergrad Knowledge',
        'h','h'
    )

    figure = px.bar(
        factors_df['Career Aspirations'].value_counts(), 
        title='Student Career Aspirations During Undergrad', 
        orientation = 'h'
    )

    figure.update_layout(
        plot_bgcolor = "rgba(0,0,0,0)",
        xaxis = (dict(showgrid=False))
    )

    st.plotly_chart(figure)

elif selected == "Logout":

    os.system("taskkill /im firefox.exe /f")
    os.system("taskkill /im chrome.exe /f")
    os.system("taskkill /im brave.exe /f")

    webbrowser.open("https://isj107vee.github.io/login/")

#----------------------------------Styling-----------------------------------
hide_st_style = """
       
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)