import sheet

# プレイヤーを追加
def add_player(id, name):
    id = str(id)
    row = sheet.find_row('PlayerList', id, 1)
    if row > 0:
        sheet.update_cell('PlayerList', row, 1, id)
        sheet.update_cell('PlayerList', row, 2, name)
        print("更新")
    else:
        sheet.append_row('PlayerList', [id, name])    
        print("追加")

# プレイヤーを削除
def remove_player(id, name):
    id = str(id)
    row = sheet.find_row('PlayerList', id, 1)
    if row > 0:
        sheet.delete_row('PlayerList', row)
        return True
    else:
        return False