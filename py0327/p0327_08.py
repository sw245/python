
# list 타입 - 배열

# fruit = ['사과','배','딸기','포도']

# print(fruit[0])
# print(fruit)

# fruit_name = input("과일 이름을 입력하십시오.")

# if fruit_name in fruit:
#     print("있습니다.")
# else:
#     print("없습니다.")
    

# fruit = ['사과','배','딸기','포도']
# print(fruit[0])
# print(fruit[1])
# print(fruit[2])
# print(fruit[3])

# item = [
#     {"galContentId":"3479214","galContentTypeId":"17","galTitle":"통영 중앙전통시장","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/14/3479214.jpg","galCreatedtime":"20250219140831","galModifiedtime":"20250219141444","galPhotographyMonth":"202412","galPhotographyLocation":"경상남도 통영시 중앙동","galPhotographer":"한국관광공사 김지호","galSearchKeyword":"통영 중앙전통시장, 경상남도 통영시, 상설시장"},
#     {"galContentId":"3479203","galContentTypeId":"17","galTitle":"통영 이순신공원","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/03/3479203.jpg","galCreatedtime":"20250219134652","galModifiedtime":"20250219140236","galPhotographyMonth":"202412","galPhotographyLocation":"경상남도 통영시 정량동","galPhotographer":"한국관광공사 김지호","galSearchKeyword":"통영 이순신공원, 경상남도 통영시, 테마공원, 한산대첩기념공원, 산책로, 산책길, 걷기여행"},
#     {"galContentId":"3479186","galContentTypeId":"17","galTitle":"통영RCE세자트라숲","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/86/3479186.jpg","galCreatedtime":"20250219110501","galModifiedtime":"20250219111852","galPhotographyMonth":"202412","galPhotographyLocation":"경상남도 통영시 용남면","galPhotographer":"한국관광공사 김지호","galSearchKeyword":"통영RCE세자트라숲, 경상남도 통영시, 자연생태관광지, 가을, 단풍, 추경, 산책로, 산책길, 걷기여행, 억새"},
#     {"galContentId":"3479104","galContentTypeId":"17","galTitle":"청마문학관","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/04/3479104.jpg","galCreatedtime":"20250218155721","galModifiedtime":"20250218160842","galPhotographyMonth":"202412","galPhotographyLocation":"경상남도 통영시 정량동","galPhotographer":"한국관광공사 김지호","galSearchKeyword":"청마문학관, 경상남도 통영시, 전시관, 유치환 생가 복원지, 초가집, 파노라마"},
#     {"galContentId":"3479084","galContentTypeId":"17","galTitle":"강구안","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/84/3479084.jpg","galCreatedtime":"20250218153802","galModifiedtime":"20250218154430","galPhotographyMonth":"202412","galPhotographyLocation":"경상남도 통영시 동호동","galPhotographer":"한국관광공사 김지호","galSearchKeyword":"강구안, 경상남도 통영시, 항구, 남해, 바다, 강구안 보도교, 조선군선, 판옥선, 전라좌수영거북선, 파노라마"},
#     {"galContentId":"3479075","galContentTypeId":"17","galTitle":"고성공룡박물관","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/75/3479075.jpg","galCreatedtime":"20250218152602","galModifiedtime":"20250218153330","galPhotographyMonth":"202412","galPhotographyLocation":"경상남도 고성군 하이면","galPhotographer":"한국관광공사 김지호","galSearchKeyword":"고성공룡박물관, 경상남도 고성군, 전시관, 상족암군립공원, 가을, 단풍, 추경, 남해, 바다, 드론촬영, 드론사진, 항공촬영"},
#     {"galContentId":"3479067","galContentTypeId":"17","galTitle":"상족암군립공원","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/67/3479067.jpg","galCreatedtime":"20250218151332","galModifiedtime":"20250218152047","galPhotographyMonth":"202412","galPhotographyLocation":"경상남도 고성군 하이면","galPhotographer":"한국관광공사 김지호","galSearchKeyword":"상족암군립공원, 경상남도 고성군, 자연공원, 고성 덕명리 공룡과 새발자국화석 산지, 국가유산, 자연유산, 천연기념물 제411호, 몽돌해변, 남해, 바다, 드론촬영, 드론사진, 항공촬영"},
#     {"galContentId":"3469888","galContentTypeId":"17","galTitle":"운림산방","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/88/3469888.jpg","galCreatedtime":"20250123111151","galModifiedtime":"20250218090238","galPhotographyMonth":"202411","galPhotographyLocation":"전라남도 진도군 의신면","galPhotographer":"강시몬","galSearchKeyword":"운림산방, 전라남도 진도군, 국가유산, 자연유산, 명승 제80호, 연못, 드론촬영, 드론사진, 항공촬영, 11월 버킷, 11월 추천여행지, 사진기자단, 프레임코리아2기"},
#     {"galContentId":"3470649","galContentTypeId":"17","galTitle":"단양 구인사","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/49/3470649.jpg","galCreatedtime":"20250123173002","galModifiedtime":"20250218090238","galPhotographyMonth":"202411","galPhotographyLocation":"충청북도 단양군 영춘면","galPhotographer":"강윤구","galSearchKeyword":"단양 구인사, 충청북도 단양군, 절, 사찰, 불교, 종교, 가을, 단풍, 추경, 11월 추천여행지, 사진기자단, 프레임코리아2기"},
#     {"galContentId":"3470674","galContentTypeId":"17","galTitle":"단양 보발재","galWebImageUrl":"http://tong.visitkorea.or.kr/cms2/website/74/3470674.jpg","galCreatedtime":"20250123173649","galModifiedtime":"20250218090238","galPhotographyMonth":"202411","galPhotographyLocation":"충청북도 단양군 가곡면","galPhotographer":"강윤구","galSearchKeyword":"단양 보발재, 충청북도 단양군, 드라이브코스, 고드너머재, 단풍, 가을, 추경, 드론촬영, 드론사진, 항공촬영, 11월 추천여행지, 사진기자단, 프레임코리아2기"}
# ]

# print(item[6]['galTitle'])

num = [1,2,3,4,5,6,7,8,9,10]

print(num[2]+num[4]+num[6]+num[8])

in_num = int(input("숫자를 입력하세요 >"))
if in_num in num:
    print(f"{in_num}는 있습니다.")
else:
    print(f"{in_num}는 없습니다.")