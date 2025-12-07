#!/usr/bin/env python3
"""
香港六合彩號碼生成器
Hong Kong Mark Six Lottery Number Generator

規則:
第1至第8注: 任選48個號碼買八注（不可重覆）
第9注: 第49個號碼＋任意的5個號碼
第10至第16注: 不用第9注的5個任意號碼，在剩下的44個號碼裏選42個字買七注（不可重覆）
第17注: 在上面剩下的兩個號碼再配搭任意四個號碼
"""

import random


def generate_mark_six_numbers():
    """生成17注六合彩號碼"""
    
    results = []
    
    # ========================================
    # 第1至第8注: 任選48個號碼買八注（不可重覆）
    # ========================================
    # 1-48號，共48個號碼
    first_48 = list(range(1, 49))
    random.shuffle(first_48)
    
    # 將48個號碼分成8注，每注6個
    for i in range(8):
        bet = sorted(first_48[i*6 : (i+1)*6])
        results.append(bet)
    
    # ========================================
    # 第9注: 第49個號碼＋任意的5個號碼
    # ========================================
    # 第49個號碼 = 49
    the_49th = 49
    # 從1-48中隨機選5個作為「任意的5個號碼」
    arbitrary_5 = random.sample(first_48, 5)
    bet_9 = sorted([the_49th] + arbitrary_5)
    results.append(bet_9)
    
    # ========================================
    # 第10至第16注: 不用第9注的5個任意號碼，
    # 在剩下的44個號碼裏選42個字買七注（不可重覆）
    # ========================================
    # 剩下的44個號碼 = 1-49 減去 5個任意號碼
    all_49 = list(range(1, 50))
    remaining_44 = [n for n in all_49 if n not in arbitrary_5]
    
    # 從44個中選42個
    selected_42 = random.sample(remaining_44, 42)
    remaining_2 = [n for n in remaining_44 if n not in selected_42]
    
    # 將42個號碼分成7注，每注6個
    random.shuffle(selected_42)
    for i in range(7):
        bet = sorted(selected_42[i*6 : (i+1)*6])
        results.append(bet)
    
    # ========================================
    # 第17注: 在上面剩下的兩個號碼再配搭任意四個號碼
    # ========================================
    # 任意4個號碼（從所有49個中排除這2個後選取）
    pool_for_4 = [n for n in all_49 if n not in remaining_2]
    arbitrary_4 = random.sample(pool_for_4, 4)
    bet_17 = sorted(remaining_2 + arbitrary_4)
    results.append(bet_17)
    
    return results, {
        'first_48': sorted(first_48),
        'the_49th': the_49th,
        'arbitrary_5_in_bet9': sorted(arbitrary_5),
        'remaining_44': sorted(remaining_44),
        'selected_42': sorted(selected_42),
        'remaining_2': sorted(remaining_2),
        'arbitrary_4_in_bet17': sorted(arbitrary_4)
    }


def print_results(results, info):
    """美觀地印出結果"""
    
    print("=" * 60)
    print("           香港六合彩號碼生成器 - 17注")
    print("=" * 60)
    print()
    
    # 第1-8注
    print("【第1至第8注】從48個號碼中分配（不重覆）")
    print("-" * 40)
    for i in range(8):
        numbers_str = "  ".join(f"{n:02d}" for n in results[i])
        print(f"  第 {i+1:2d} 注: {numbers_str}")
    print()
    
    # 第9注
    print(f"【第9注】第49個號碼({info['the_49th']:02d}) + 任意5個號碼")
    print("-" * 40)
    numbers_str = "  ".join(f"{n:02d}" for n in results[8])
    print(f"  第  9 注: {numbers_str}")
    print(f"  （任意5個: {', '.join(f'{n:02d}' for n in info['arbitrary_5_in_bet9'])}）")
    print()
    
    # 第10-16注
    print("【第10至第16注】從剩餘44個號碼中選42個分配（不重覆）")
    print("-" * 40)
    for i in range(9, 16):
        numbers_str = "  ".join(f"{n:02d}" for n in results[i])
        print(f"  第 {i+1:2d} 注: {numbers_str}")
    print()
    
    # 第17注
    print(f"【第17注】剩餘2個號碼 + 任意4個號碼")
    print("-" * 40)
    numbers_str = "  ".join(f"{n:02d}" for n in results[16])
    print(f"  第 17 注: {numbers_str}")
    print(f"  （剩餘2個: {', '.join(f'{n:02d}' for n in info['remaining_2'])}）")
    print(f"  （任意4個: {', '.join(f'{n:02d}' for n in info['arbitrary_4_in_bet17'])}）")
    print()
    
    print("=" * 60)
    print("                    祝你好運！")
    print("=" * 60)


def main():
    results, info = generate_mark_six_numbers()
    print_results(results, info)
    
    # 驗證
    print("\n【驗證資訊】")
    print(f"  第1-8注使用的48個號碼: {info['first_48']}")
    print(f"  第49個號碼: {info['the_49th']}")
    print(f"  第10-16注排除的5個號碼: {info['arbitrary_5_in_bet9']}")
    print(f"  第10-16注使用的42個號碼: {info['selected_42']}")
    print(f"  第17注的剩餘2個號碼: {info['remaining_2']}")


if __name__ == "__main__":
    main()
