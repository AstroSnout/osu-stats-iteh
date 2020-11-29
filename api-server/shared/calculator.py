from collections import namedtuple


def num_to_mod(number):
    number = int(number)
    mod_list = []

    if number & 1 << 0:   mod_list.append('NF')
    if number & 1 << 1:   mod_list.append('EZ')
    if number & 1 << 3:   mod_list.append('HD')
    if number & 1 << 4:   mod_list.append('HR')
    if number & 1 << 5:   mod_list.append('SD')
    if number & 1 << 9:   mod_list.append('NC')
    elif number & 1 << 6: mod_list.append('DT')
    if number & 1 << 7:   mod_list.append('RX')
    if number & 1 << 8:   mod_list.append('HT')
    if number & 1 << 10:  mod_list.append('FL')
    if number & 1 << 12:  mod_list.append('SO')
    if number & 1 << 14:  mod_list.append('PF')
    if number & 1 << 15:  mod_list.append('4 KEY')
    if number & 1 << 16:  mod_list.append('5 KEY')
    if number & 1 << 17:  mod_list.append('6 KEY')
    if number & 1 << 18:  mod_list.append('7 KEY')
    if number & 1 << 19:  mod_list.append('8 KEY')
    if number & 1 << 20:  mod_list.append('FI')
    if number & 1 << 24:  mod_list.append('9 KEY')
    if number & 1 << 25:  mod_list.append('10 KEY')
    if number & 1 << 26:  mod_list.append('1 KEY')
    if number & 1 << 27:  mod_list.append('3 KEY')
    if number & 1 << 28:  mod_list.append('2 KEY')

    return mod_list


def everything(beatmap_id, all_plays):
    # Return variables
    Result = namedtuple('Result', 'occurrence count pp_avg acc_avg')

    # Helpers
    users = []
    play_pp = []
    play_accs = []

    count = 0
    # The loop
    for play in all_plays:
        # Checks for map
        if play.beatmap_id == beatmap_id:
            count += 1
            # Used for accuracy calculation
            hit300 = int(play.count300) + int(play.countgeki)
            hit100 = int(play.count100) + int(play.countkatu)
            hit50 = int(play.count50)
            miss = int(play.countmiss)
            hit_total = hit300 + hit100 + hit50 + miss

            acc_top = 50 * hit50 + 100 * hit100 + 300 * hit300
            acc_bot = 300 * hit_total
            acc_coef = acc_top / acc_bot
            map_acc = acc_coef * 100
            play_accs.append(map_acc)
            play_pp.append(float(play.pp))

        # Used for occurrence calculation
        if play.user_id not in users:
            users.append(play.user_id)


    # Calculations

    occurrence = round((count / len(users)) * 100, 2)
    pp_avg = round(sum(play_pp) / len(play_pp), 2)
    acc_avg = round(sum(play_accs) / len(play_accs), 2)

    return Result(occurrence, count, pp_avg, acc_avg)


def difficulty_percentage(diff_spd, diff_aim):
    diff_spd = float(diff_spd)
    diff_aim = float(diff_aim)
    total = diff_aim + diff_spd
    aim_pct = round((diff_aim/total) * 100)
    spd_pct = 100 - aim_pct
    return aim_pct, spd_pct
