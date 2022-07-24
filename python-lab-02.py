

# Program heading
print('The Test Scores Program')
print()
print('Enter 3 test scores')
print('==============================')
test1=int(input('Enter test score: ')) # Assigns the inputed value to test score. 
test2=int(input('Enter test score: '))
test3=int(input('Enter test score: '))
print('==============================')

# Calculate total test scores and averages.
totalScore=test1 + test2 +test3
print('The Total Test Score:', totalScore)
averageScore= float(totalScore/3)
print('Average Score:', averageScore)
print()
print('BYE')
print()