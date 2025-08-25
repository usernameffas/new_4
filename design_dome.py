# -*- coding: utf-8 -*-
# math 라이브러리에서 pi 값을 사용하기 위해 import 합니다.
import math

# 최종 계산 결과를 저장할 전역 변수들입니다.
# 이 변수들은 sphere_area 함수에 의해 업데이트됩니다.
material = ''
diameter = 0.0
thickness = 0.0
area = 0.0
weight = 0.0

# 재료별 밀도(g/cm^3)를 정의한 딕셔너리입니다.
# 이를 통해 향후 새로운 재료를 쉽게 추가할 수 있습니다.
MATERIAL_DENSITIES = {
    '유리': 2.4,
    '알루미늄': 2.7,
    '탄소강': 7.85
}

# 화성의 중력을 지구 중력에 대한 비율로 나타낸 값입니다.
# 화성의 중력은 지구 중력의 약 37.8%입니다.
MARS_GRAVITY_RATIO = 0.378

def sphere_area(dome_diameter, material_name='유리', dome_thickness=1):
    """
    화성 기지 돔(반구체)의 표면적과 무게를 계산합니다.

    매개변수:
    - dome_diameter (float): 돔의 지름(미터)입니다.
    - material_name (str): 돔의 재질입니다 ('유리', '알루미늄', '탄소강').
                           기본값은 '유리'입니다.
    - dome_thickness (float): 돔의 두께(센티미터)입니다.
                              기본값은 1cm입니다.
    """
    # 전역 변수들을 수정하기 위해 'global' 키워드를 사용합니다.
    global material, diameter, thickness, area, weight

    # 지름이 유효한 양수인지 확인합니다.
    if dome_diameter <= 0:
        print('오류: 지름은 0보다 커야 합니다.')
        return

    # 두께가 유효한 양수인지 확인합니다.
    if dome_thickness <= 0:
        print('오류: 두께는 0보다 커야 합니다.')
        return

    # 입력된 매개변수를 전역 변수에 할당합니다.
    material = material_name
    diameter = dome_diameter
    thickness = dome_thickness

    # 1단계: 돔(반구체)의 표면적을 계산합니다.
    # 구의 표면적 공식은 4 * pi * r^2 입니다.
    # 반구(돔)의 경우, 절반인 2 * pi * r^2 입니다.
    # 지름을 통해 반지름을 구합니다 (반지름 = 지름 / 2).
    radius = dome_diameter / 2
    dome_area_m2 = 2 * math.pi * (radius ** 2)

    # 2단계: 재료의 밀도를 가져옵니다. 재료 이름을 찾을 수 없으면 기본값인 '유리'를 사용합니다.
    density_g_cm3 = MATERIAL_DENSITIES.get(material_name, MATERIAL_DENSITIES['유리'])

    # 3단계: 일관된 계산을 위해 단위를 변환합니다.
    # 두께를 cm에서 미터로 변환합니다.
    thickness_m = dome_thickness / 100

    # 밀도를 g/cm^3에서 kg/m^3으로 변환합니다.
    # 1 g/cm^3 = 1000 kg/m^3 입니다.
    density_kg_m3 = density_g_cm3 * 1000

    # 4단계: 돔 재료의 부피를 계산합니다.
    # 부피 = 표면적 * 두께 입니다.
    dome_volume_m3 = dome_area_m2 * thickness_m

    # 5단계: 화성에서의 무게를 계산합니다.
    # 먼저 지구에서의 무게를 계산합니다.
    earth_weight_kg = dome_volume_m3 * density_kg_m3
    
    # 그 다음, 화성 중력 비율을 적용합니다.
    mars_weight_kg = earth_weight_kg * MARS_GRAVITY_RATIO

    # 6단계: 계산 결과를 소수점 셋째 자리까지 반올림하여 전역 변수에 저장합니다.
    area = round(dome_area_m2, 3)
    weight = round(mars_weight_kg, 3)

def main():
    """
    돔 계산 프로그램의 메인 함수입니다.
    사용자 입력을 처리하고 반복적인 계산을 위한 루프를 실행합니다.
    """
    print('### 화성 기지 돔 면적 및 무게 계산기 ###')
    print('계산 종료를 원하시면 언제든지 "종료"를 입력하세요.')
    print('-------------------------------------------')

    while True:
        try:
            # 지름, 재질, 두께에 대한 사용자 입력을 받습니다.
            input_diameter_str = input('돔의 지름(m)을 입력하세요: ')
            if input_diameter_str == '종료':
                break

            input_material_str = input('재질을 입력하세요 (유리, 알루미늄, 탄소강) [기본값: 유리]: ')
            if input_material_str == '종료':
                break
                
            input_thickness_str = input('두께(cm)를 입력하세요 [기본값: 1]: ')
            if input_thickness_str == '종료':
                break

            # 사용자 입력을 적절한 데이터 타입으로 변환합니다.
            # 입력이 없을 경우 기본값을 사용합니다.
            diameter_val = float(input_diameter_str)
            material_val = input_material_str if input_material_str else '유리'
            thickness_val = float(input_thickness_str) if input_thickness_str else 1.0

            # 사용자 값으로 sphere_area 함수를 호출합니다.
            sphere_area(diameter_val, material_val, thickness_val)

            # 계산이 성공적으로 완료되었는지 확인하고 결과를 출력합니다.
            # 지름이 0 이하일 경우 함수가 조기 종료됩니다.
            if diameter > 0 and thickness > 0:
                print('-------------------------------------------')
                print(f'재질 =⇒ {material}, 지름 =⇒ {round(diameter, 3)}, 두께 =⇒ {round(thickness, 3)}, '
                      f'면적 =⇒ {area}, 무게 =⇒ {weight} kg')
                print('-------------------------------------------')

        except ValueError:
            # 사용자가 지름이나 두께에 숫자가 아닌 값을 입력했을 때 예외를 처리합니다.
            print('오류: 지름 또는 두께에 올바른 숫자 값을 입력하세요.')

    print('\n계산기를 종료합니다.')

# 스크립트가 직접 실행될 때 main 함수가 호출되도록 합니다.
if __name__ == '__main__':
    main()
