#! /bin/bash




#prints user possible commands
echo "Entrez une commande"
echo "(1) Effacer un utilisateur quelconque et ses répertoires étant associés"
echo "(2) Afficher les ouvertures de session"
echo "(3) Afficher les n fichiers les plus volumineux"
read com

#command 1
if [[ $com = 1 ]]; then
	#program 1
	echo "Entrez le nom de l'utilisateur que vous voulez effacer : "
	read username
	x=$(find / -user $username 2> /dev/null)
	for dir in $x; do
		chown root $dir
	done
	sudo userdel -r $username 2> /dev/null
	
	
	#command 2
elif [[ $com = 2 ]]; then
	#program 2

	echo "format = <MMM JJ>"
	echo "Entrez la date depuis laquelle vous voulez voir les utilisateurs qui ont ouvert une session :"
	read date

	# takes current year as well as the users day and month
	month=${date:0:3}
	day=${date:4}
	year=$(date +%Y)


	# turns the users month input into a month value (1-12)
	if [[ $month = 'dec' ]]; then
		month=12
	elif [[ $month = 'nov' ]]; then
		month=11
	elif [[ $month = 'oct' ]]; then
		month=10
	elif [[ $month = 'sep' ]]; then
		month=9
	elif [[ $month = 'aug' ]]; then
		month=8
	elif [[ $month = 'jul' ]]; then
		month=7
	elif [[ $month = 'jun' ]]; then
		month=6
	elif [[ $month = 'may' ]]; then
		month=5
	elif [[ $month = 'apr' ]]; then
		month=4
	elif [[ $month = 'mar' ]]; then
		month=3
	elif [[ $month = 'feb' ]]; then
		month=2
	elif [[ $month = 'jan' ]]; then
		month=1
	fi
	
	
	# creates text files to work on 
	touch f1.txt
	touch f2.txt
	
	
	# this command lists all the lines of the users activities and opened sessions, removes unecessary last line, adds everything to 
	# the text file f1.txt
	last -s $year-$month-$day -t now | head -n -1 > f1.txt
	
	# from last command, takes all lines, and takes only the users from the strings, results are dumped in f2.txt
	awk '{print $1;}' f1.txt > f2.txt
	
	# removes duplicates and sorts, dumped back into f1.txt
	sort -u f2.txt > f1.txt
	
	# reboot is not a user but will apear, command removes 'reboot' instances
	sed '/reboot/d' f1.txt > f2.txt
	
	# prints all users
	cat f2.txt
	
	# removes previous text files
	rm f2.txt
	rm f1.txt



	
	
	#command 3
elif [[ $com = 3 ]]; then
	#program 3
	echo "Entrez le nombre de gros fichier a afficher"
	read n
	find -type f -exec du -sh {} + | sort -rh | head -n $n	
else
	echo "invalid command.."
fi






