from app.model.race import Race

race = Race()
race.load_race_log()
race.build_race_history_from_log()
race.scoreboard()
race.race_curiosities()
