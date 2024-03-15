def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.read.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(np.mean(df[df['sex']=='Male']),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df[df['education'] == 'Bachelors'].shape[0]/df.shape[0])*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # # with and without `Bachelors`, `Masters`, or `Doctorate`
    # higher_education = None
    # lower_education = None

    # # percentage with salary >50K
    # higher_education_rich = None
    # lower_education_rich = None


    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df['hours-per-week'])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]

    rich_percentage = num_min_workers/df.shape[0]*100

