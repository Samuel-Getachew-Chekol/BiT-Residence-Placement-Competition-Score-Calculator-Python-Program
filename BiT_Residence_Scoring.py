#The following function, called date_calculator(), calculates how many years a person served in the university and how
#....many years in a certain position.
def date_calculator():
    print('Receiving service duration.\nSAMPLE of DATE entry ==> date/month/year')
    starting_date=input('From: ')
    end_date=input('  To: ')
    starting_date_list=starting_date.split('/')
    end_date_list=end_date.split('/')
    number_of_days=int(end_date_list[0])-int(starting_date_list[0])
    number_of_months=int(end_date_list[1])-int(starting_date_list[1])
    number_of_years=int(end_date_list[2])-int(starting_date_list[2])
    if number_of_days<0:
        number_of_days+=30
        number_of_months=int(end_date_list[1])-1-int(starting_date_list[1])
        if number_of_months<0:
            number_of_months+=12
            number_of_years=int(end_date_list[2])-1-int(starting_date_list[2])
    if number_of_months < 0:
        number_of_months += 12
        number_of_years = int(end_date_list[2]) - 1 - int(starting_date_list[2])
    if number_of_years<0:
        number_of_years=0
    if end_date_list[2]>starting_date_list[2]:
        number_of_days+=5
    service_years=(number_of_days/365)+(number_of_months/12)+(number_of_years)
    print(f'********'
          f'\nYou served for {number_of_years} years {number_of_months} months and {number_of_days} days .'
          f'\n+++ service years = {str(service_years)}')
    return service_years
#The ff function called cademic_rank_point(), calculates the amount of points to be awarded to a person based on his/her...
#...academic level
def academic_rank_point():
    print("Here below the words to be entered are listed. Please enter the correct number based on the following manual.\n"
          "                        Professor=30\n"
          "              Associate Professor=27\n"
          "              Assistant Professor=24\n"
          "                         Lecturer=21\n"
          "               Assistant Lecturer=18\n"
          "            Graduate Assistant II=15\n"
          "             Graduate Assistant I=12\n"
          "Chief Technical Assistant II(PhD)=21\n"
          "Chief Technical Assistant I (MSc)=18\n"
          "       Senior Technical Assistant=15\n"
          "       Junior Technical Assistant=12\n")
    print('Taking Academic Rank points (30%)')
    while True:
       value = input('Enter your Academic Rank Value: ')
       try:
           academic_rank=int(value)
           print(f'Your Academic rank point= {academic_rank}')
           return academic_rank
       except ValueError:
           print('Error! Please enter the right number only. For more please see the above manual. Enter again')
total_academic_status_point = academic_rank_point()
#The ff function decides how much points are to be awarded to a person for his/her total service years...
#...It works by calling the previous date_calculator() function.
def service_year():
    print('Taking service year points (25%)')
    service_year_points=date_calculator()
    if 0<service_year_points<=15:
        service_year_points=service_year_points*25/15
        return service_year_points
    elif service_year_points>15:
        service_year_points=25
        return service_year_points
total_service_years_point = service_year()
#The ff function outputs the total points a person has to be awarded for his/her service to the university by incorporating...
#...the date_calculator() function, the input() function and the universities bylaw on the award of points.
def university_position():
    count = 0
    total = 0
    pv = 0
    position_type = ['president', 'vice president', 'dean', 'director', 'vice dean', 'department head', 'chair holder'
                     'vice department head', 'course chair',
                     'teachers rep.', 'batch advisor']
    print('Taking university position points (15%).\n'
          'Please enter the position types only listed below.\n'
          'Spell carefully\n',position_type)
    try:
        for i in position_type:
            pt = input('Enter the position type you served on: ')
            if pt == 'done' or pt == 0:
                if 0 < total <= 15:
                    print(f'Your position point= {total}\n')
                    all_info['University position score=']=all_info.get('University position score=',0)+total
                    return total
                elif total > 15:
                    total = 15
                    print(f'Your position point= {total}\n')
                    return total
            elif pt in position_type:
                if pt == 'president':
                    yr = date_calculator()
                    if yr < 6:
                        pv = yr * 15 / 6
                    elif yr >= 6:
                        pv = 15
                elif pt == 'vice president':
                    yr = date_calculator()
                    if yr < 3:
                        pv = yr * 13 / 3
                    elif yr >= 3:
                        pv = 13
                elif pt == 'dean' or pt == 'dean':
                    yr = date_calculator()
                    if yr < 3:
                        pv = yr * 11 / 3
                    elif yr >= 3:
                        pv = 11
                elif pt == 'vice dean':
                    yr = date_calculator()
                    if yr < 3:
                        pv = yr * 9 / 3
                    elif yr >= 3:
                        pv = 9
                elif pt == 'department head' or pt == 'chair holder':
                    yr = date_calculator()
                    if yr < 3:
                        pv = yr * 7 / 3
                    elif yr >= 3:
                        pv = 7
                elif pt == 'vice department head':
                    yr = date_calculator()
                    if yr < 3:
                        pv = yr * 5 / 3
                    elif yr >= 3:
                        pv = 5
                elif pt == 'course chair':
                    yr = date_calculator()
                    if yr < 1:
                        pv = yr * 3 / 2
                    elif yr >= 2:
                        pv = 3
                elif pt == 'teachers rep.':
                    yr = date_calculator()
                    if yr < 3:
                        pv = yr * 5 / 3
                    elif yr >= 3:
                        pv = 5
                elif pt == 'batch advisor':
                    yr = int(input('Enter The number of Semesters You Served as a Batch Advisors: '))
                    pv = yr / 4
                count = count + 1
                total = total + pv
                print('Your position point= ', total, 'Number of positions= ', count)
            else:
                print('Error! Please see the manual and carefully enter the type(s) of position you have served on.')
    except:
        print('Error, Please read the above manual')
    return total
total_university_position_point = university_position()
#The ff function called teaching_efficiency() takes in the latest year efficiency points scored by the person and ...
#... outputs the points it is equivalent to.
def teaching_efficiency():
    print('Taking Teaching Efficiency (5%)')
    te=float(input('Enter your teaching efficiency: '))
    te=float(te)*5/100
    if te>5:
        print('Error! Only enter number values between 0 and 5.')
    if 0<=te<=5:
        print(f'Teaching efficiency= {te}\n')
    return te
total_efficiency_point = teaching_efficiency()
#pub_rate_calc() calculates the rating of the publications a person has based on the university's legislation...
#...these rates are multiplied by the weight of the publication as it is written in the preceeding function.
def pub_rate_calc():
    rate=0
    r=0
    while True:
        num_auth = input('Enter the number of authors who took part in your publication: ')
        rate=rate+r
        #print('Rate= ')
        #return rate
        if num_auth=='done':
            return rate
        try:
            num_auth=float(num_auth)
            if num_auth == 1:
                r= 1
            elif num_auth == 2:
                auth_rank = int(input('Which number author were you?\nEnter only the numbers.: '))
                if auth_rank == 1:
                    r = 0.8
                else:
                    r= 0.75
            elif num_auth == 3:
                auth_rank = int(input('Which number author were you?\nEnter only the numbers.: '))
                if auth_rank == 1:
                    r= 0.7
                else:
                    r= 0.65
            elif num_auth == 4:
                auth_rank = int(input('Which number author were you?\nEnter only the numbers.: '))
                if auth_rank == 1:
                    r= 0.6
                else:
                    r= 0.55
            elif num_auth >= 5:
                auth_rank = int(input('Which number author were you?\nEnter only the numbers.: '))
                if auth_rank == 1:
                    r= 0.5
                else:
                    r= 0.45
        except:
            print('Error, Please read the above manual')
#the ff function takes pu_rate_calc() as an input and finds out the total points a person deserves...
#... different publication types have different weights
def publication_points():
    print('Taking publication points\n'
          'Please look the following guideline and accordingly enter the inputs.\n'
          'For articles enter article\n'
          'For review article review\n'
          'For conference papers enter conference\n'
          'For patents and copyrights enter patent or copyright\n')
    pub_pnt = 0
    i=0
    while True:
        pub_type = input('What kind of publications do you have?: ')
        pub_pnt=pub_pnt+i
        if pub_type=='done' or pub_type=='0':
            if pub_pnt>15:
                pub_pnt=15
            print(f'Your publication point= {pub_pnt}\n')
            return pub_pnt
        elif pub_type=='article':
            i=3*pub_rate_calc()
        elif pub_pnt=='review article':
            i = 1.5 * pub_rate_calc()
        elif pub_type=='conference':
            i=1.5*pub_rate_calc()
        elif pub_type=='patent' or pub_type=='copyright':
            i=1.5*pub_rate_calc()
total_publication_point = publication_points()
#the ff function takes in the number of valid certifications a person has been awarded by the university's community ...
#...engagement diractorate. It outputs the points the person's certifications deserve.
def community_service():
    print('Taking Community service points (5%)')
    while True:
        cs = input('Enter the number of community service certificates you earned: ')
        try:
            cs=int(cs)
            print(f'Your community service point= {cs}\n')
            return cs
        except:
            print('Error! Enter integeral values only')
total_community_service_point = community_service()
#the ff function decides which points deserve to which kind of family status a person has.
def family_point():
    print('Taking marriage situation points (5%)\n'
          '    Married and have kids=mhk\n'
          '   Unmarried and have kid=umhk\n'
          ' Married and have no kids=m\n'
          '                   single=s')
    while True:
        fp = input('Enter your marriage situation: ')
        if fp == 'mhk':
            print(f'Your family point= 5\n')
            return 5
        elif fp == 'umhk':
            print(f'Your family point= 4\n')
            return 4
        elif fp == 'm':
            print(f'Your family point= 3\n')
            return 3
        elif fp == 's':
            print(f'Your family point= 2\n')
            return 2
        else:
            print('Error! Enter the words shown in the above manual only.')
total_family_point = family_point()
#the ff function gives points to applicants who are female and/or physically impaired.
def affirmative_points():
    print('Taking gender point\n if Man enter m\n if Woman enter w')
    gen_type=input('Enter gender type: ')
    if gen_type=='m' or gen_type=='M':
        gen_point=0
    elif gen_type=='w' or gen_type=='W':
        gen_point=3
    p_i=input('Do you have any physical impairment? (Enter yes or no): ')
    if p_i=='yes':
        p_i_p=4
    else:
        p_i_p=0
    m_s=input('Are you married with a lecturer in BDU? (Enter yes or no): ')
    if m_s == 'yes':
        m_s_p=5
    else:
        m_s_p=0
    aff_points = gen_point + p_i_p + m_s_p
    print(f'Your affirmative points= {aff_points}\n')
    return aff_points
total_affirmative_point = affirmative_points()
total_points = total_academic_status_point + total_service_years_point + total_university_position_point + total_efficiency_point + total_publication_point + total_community_service_point + total_family_point + total_affirmative_point

with open(f'{applicants_name}_{id_no}.txt', 'w') as file:
    #file_of_applicant=open(f"{applicants_name}_{id_no}.txt", 'w')
    file.write(f'Applicants Name: {applicants_name}'
               f'\nId. Number: {id_no}'
               f'\nInstitute: {campus}'
               f'\nDepartment: {dept}'
               f'\n********'
               f'\n             Total academic rank points = {total_academic_status_point}'
               f'\n             Total service year points = {total_service_years_point}'
               f'\n             Total university position points = {total_university_position_point}'
               f'\n             Total teaching efficiency points = {total_efficiency_point}'
               f'\n             Total publication points = {total_publication_point}'
               f'\n             Total community service points = {total_community_service_point}'
               f'\n             Total family points = {total_family_point}'
               f'\n             Total affirmative points = {total_affirmative_point}'
               f'\n             ********************************************************************'
               f'\n             Sum of all points = {total_points}.'
               f'\n             ********************************************************************'
               )
