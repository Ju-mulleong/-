#태양과 지구의 평균 거리는 149,597,870km이다. 빛이 1초에 299.792km를 이동한다고 가정할 때
#태양에서 출발한 빛이 지구에 도착하는데 걸리는 시간은 몇 초인가? 
#또, 이 값을 분으로 환산하여 보라

distance = 149597870
speed_of_light = 299792
time_second = distance/speed_of_light
time_minute = distance/(speed_of_light*60)
print(time_second)
print(time_minute)