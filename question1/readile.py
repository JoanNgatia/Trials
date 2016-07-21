from __future__ import division


def education_report(index):
    """Func- take in index to start and find 100 records from the index.

    Open csv file to access records
    params:
    - index - value to start from
    Find 100 next records from the index.
    """
    attended_bootcamp = 0
    no_bootcamp = 0
    all_majors = []
    school_majors = []
    education_level = []
    owe_debt = []
    degrees_levels = ["Ph.D.", "master's degree (non-professional)",
                      "bachelor's degree", "associate\'s degree", " no degree",
                      "high school diploma or equivalent (GED)",
                      "some high school",
                      "no high school (secondary school)",
                      ]
    levels = []
    data = open("data.csv").readlines()
    for val in range(index, int(index) + 10):
        # Retrieve info for each of the coders in lists for each.
        final_data = data[val].split(",")

        # get highest level of education and compare with defined levels.
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
            all_majors.append(school_majors.count(major))

        # percentage that owe debt and average amount of debt owed
        if final_data[-1] != 'NA\n':
            owe_debt.append(int(final_data[-1].strip("\"\n")))

        # percentage of new that attended bootcamps vs those who didn't,
        if final_data[1] == '0':
            no_bootcamp = no_bootcamp + 1
        else:
            attended_bootcamp = attended_bootcamp + 1

    print "Percentage that attended bootcamps: {}%".format(attended_bootcamp / no_bootcamp * 100)
    print "Percentage owing student debt: {}%".format(len(owe_debt) / (val - len(owe_debt)) * 100)
    print "Average debt owed is: {}".format(sum(owe_debt) / len(owe_debt))
    print "Most popular school major is: {}".format(school_majors[max(all_majors)])
    print "Highest level of educatin is: {}".format(degrees_levels[min(levels)])
