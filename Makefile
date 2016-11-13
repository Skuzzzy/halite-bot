


run:
	./halite -d "30 30" "python3 ./src/pybot/MyBot.py" "python3 ./src/pybot/MyBot.py"

package:
	zip bot.zip ./src/*

clean:
	rm bot.zip & true;
	rm *.log & true;
	rm *.hlt & true;
