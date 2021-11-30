def age_calculator(year, month, day):
    import datetime
    today = datetime.datetime.now().date()
    date_of_birth = datetime.date(year, month, day)
    age = int((today - date_of_birth).days / 365.25)
    return age
    

'''
TO DO THE SAME IN C++, we'll write:

#include <iostream>
#inclute <ctime>
using namespace std;

int main(){
    int day, month, year;
    struct tm date = {0};
    cout << "Enter your date of birth(Year Month Day): ";
    cin >> year >> month >> day;
    date.tm_year = year - 1900;
    date.tm_mon = month - 1;
    date.tm_mday = day;
    time_t normal = mktime(&date);
    time_t current;
    time(&current);
    int age = (difftime(current, normal) + 86400L/2) / 86400L;
    cout << "Your age is: " << age/365<<";
    return 0;

}


'''
