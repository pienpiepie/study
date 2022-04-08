from urllib.parse import uses_params



exercise = input()
if  exercise == 'push-ups':
    METs = 8.0
elif exercise == 'sit-ups':
    METs = 8.0
elif exercise == 'squats':
    METs = 5.0
elif exercise == 'walking':
    METs = 3.3
elif exercise == 'radio-calisthenics':
    METs = 4.0
time = input()
weight = float(input())

calorie = float(time) * float(weight) * float(METs) * 1.05
print(int(calorie))