import view

team = 0
def init():
    global team
    while team <= 0 or team > 4:
        view.Сlear()
        team = view.Check(team)
        if team > 0 or team < 5:
            if team == 1:
                view.Сlear()
                view.NewEntry()
                team = 0
            if team == 2:
                view.Сlear()
                view.WholeList()
                team = view.Check(team)
                team = 0
            if team == 3:
                view.Сlear()
                view.Export()
                team = view.Check(team)
                team = 0
            if team == 4:
                view.Сlear()
                view.ImportCSV()
                team = view.Check(team)
                team = 0
