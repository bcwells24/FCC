import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")
    
    # Race count
    race_count = df['race'].value_counts()
    
    # Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    
    # Percentage with Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)
    
    # Higher and lower education
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    
    # Percentage earning >50K
    higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)
    
    # Minimum work hours
    min_work_hours = df['hours-per-week'].min()
    
    # Percentage of rich among those who work min hours
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)
    
    # Country with highest percentage of high earners
    country_salary_counts = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
    highest_earning_country = country_salary_counts[">50K"].idxmax()
    highest_earning_country_percentage = round(country_salary_counts[">50K"].max() * 100, 1)
    
    # Most popular occupation for high earners in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
