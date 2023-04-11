abbr_team = [
    ('ATL', 'Atlanta', 'Hawks'),
    ('BOS', 'Boston', 'Celtics'),
    ('CHH', 'Charlotte', 'Hornets'),
    ('CHI', 'Chicago', 'Bulls'),
    ('CLE', 'Cleveland', 'Cavaliers'),
    ('DAL', 'Dallas', 'Mavericks'),
    ('DEN', 'Denver', 'Nuggets'),
    ('DET', 'Detroit', 'Pistons'),
    ('GSW', 'Golden State', 'Warriors'),
    ('HOU', 'Houston', 'Rockets'),
    ('IND', 'Indiana', 'Pacers'),
    ('LAC', 'Los Angeles', 'Clippers'),
    ('LAL', 'Los Angeles', 'Lakers'),
    ('MIA', 'Miami', 'Heat'),
    ('MIL', 'Milwaukee', 'Bucks'),
    ('MIN', 'Minnesota', 'Timberwolves'),
    ('NJN', 'New Jersey', 'Nets'),
    ('NYK', 'New York', 'Knicks'),
    ('ORL', 'Orlando', 'Magic'),
    ('PHI', 'Philadelphia', '76ers'),
    ('PHX', 'Phoenix', 'Suns'),
    ('POR', 'Portland', 'Trail Blazers'),
    ('SAC', 'Sacramento', 'Kings'),
    ('SAS', 'San Antonio', 'Spurs'),
    ('SEA', 'Seattle', 'SuperSonics'),
    ('TOR', 'Toronto', 'Raptors'),
    ('UTA', 'Utah', 'Jazz'),
    ('VAN', 'Vancouver', 'Grizzlies'),
    ('WAS', 'Washington', 'Wizards'),
    ('MEM', 'Memphis', 'Grizzlies'),
    ('NOH', 'New Orleans', 'Hornets'),
    ('CHA', 'Charlotte', 'Hornets'),
    ('NOK', 'New Orleans/Oklahoma City', 'Hornets'),
    ('OKC', 'Oklahoma City', 'Thunder'),
    ('BKN', 'Brooklyn', 'Nets'),
    ('NOP', 'New Orleans', 'Pelicans')
]

abbr_to_team = {info[0]: info[1] + ' ' + info[2] for info in abbr_team}
city_to_team = {info[1]: info[1] + ' ' + info[2] for info in abbr_team}
# Extra corrections
city_to_team['L.A.Lakers'] = 'Los Angeles Lakers'
city_to_team['L.A.Clippers'] = 'Los Angeles Clippers'

