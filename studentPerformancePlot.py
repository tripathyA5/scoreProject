import pandas as pd
import csv
import statistics
import plotly.figure_factory as ff 
df=pd.read_csv('StudentsPerformance.csv')
fig=ff.create_distplot([df["reading score"].tolist()],['Reading Score'],show_hist=False)
scoreList = df["reading score"].tolist()
scoreMean = statistics.mean(scoreList)
scoreMedian = statistics.median(scoreList)
scoreStd= statistics.stdev(scoreList)
scoreMode = statistics.mode(scoreList)

print(scoreMode, scoreMedian, scoreMean)
score_first_std_deviation_start, score_first_std_deviation_end = scoreMean - scoreStd, scoreMean + scoreStd
score_second_std_deviation_start, score_second_std_deviation_end = scoreMean - (2*scoreStd), scoreMean + (2*scoreStd)
score_third_std_deviation_start, score_third_std_deviation_end = scoreMean - (3*scoreStd), scoreMean + (3*scoreStd)



score_list_of_data_within_1_std_deviation = [result for result in scoreList if result > score_first_std_deviation_start and result < score_first_std_deviation_end]
score_list_of_data_within_2_std_deviation = [result for result in scoreList if result > score_second_std_deviation_start and result < score_second_std_deviation_end]
score_list_of_data_within_3_std_deviation = [result for result in scoreList if result > score_third_std_deviation_start and result < score_third_std_deviation_end]
scorePercent1Std = len(score_list_of_data_within_1_std_deviation)*100/len(scoreList)
scorePercent2Std = len(score_list_of_data_within_2_std_deviation)*100/len(scoreList)
scorePercent3Std = len(score_list_of_data_within_3_std_deviation)*100/len(scoreList)

print(scorePercent1Std, scorePercent2Std, scorePercent3Std)
