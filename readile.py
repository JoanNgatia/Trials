from __future__ import division
# take in start index(n) and sift through file data to index(n + 100)


def education_report(index):
    """Func- take in index to start
       Open file
       Find 100 next records from the index"""
    attended_bootcamp = 0
    no_bootcamp = 0
    majors = []
    school_majors = []
    education_level = []
    owe_debt = []
    indices = int(index) + 10
    degrees_levels = ["Ph.D.", "master's degree (non-professional)",
                      "bachelor's degree", "associate\'s degree", " no degree",
                      "high school diploma or equivalent (GED)",
                      "some high school",
                      "no high school (secondary school)",
                      ]
    levels = []
    data = open("data.csv").readlines()
    # title = data[0]
    for val in range(index, indices):
        # Retrieve info for each of the coders in lists for each
        # final_data = list(data[val].split(","))
        final_data = data[val].split(",")
        # print data[0]
        # get highest level of education at position[-3]
        if final_data[-3] != 'NA':
            education_level.append(final_data[-3].strip("\"\n"))

        for level in education_level:
            if level in degrees_levels:
                levels.append(degrees_levels.index(level))

        # most popular school major value at position[-2]
        # get tuple of major and no of occurrences
        if final_data[-2] != 'NA':
            school_majors.append(final_data[-2])
        for major in school_majors:
            (major, school_majors.count(major))
            majors.append(school_majors.count(major))

        # percentage that owe debt and average amount of debt owed
        if final_data[-1] != 'NA\n':
            owe_debt.append(int(final_data[-1].strip("\"\n")))
        # print val - len(owe_debt)

        # percentage of new that attended bootcamps vs those who didn't,
        if final_data[1] == '0':
            no_bootcamp = no_bootcamp + 1
        else:
            attended_bootcamp = attended_bootcamp + 1
    print education_level
    print min(levels)
    print degrees_levels[min(levels)]

    # return final_data
    # print school_majors[max(majors)]
    # print max(list(school_majors.count(major)))
    # print attended_bootcamp / no_bootcamp * 100
    # print sum(owe_debt)
    # print education_level
    # print levels

education_report(10)
# print len(education_report(10))
