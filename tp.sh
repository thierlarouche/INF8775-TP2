
while getopts "a:e:pt" flag
do
    case "${flag}" in
        a) algo=${OPTARG};;
        e) path=${OPTARG};;
        p) couple="true";;
        t) timer="true";;
    esac
done

#ALGO GLOUTON
if [ $algo == "glouton" ]
then
    if [ "$couple" == 'true' ] && [ "$timer" == 'true' ]
    then
        python3 src/glouton.py $path $couple $timer

    elif [ "$couple" == "true" ]
    then
        python3 src/glouton.py $path $couple false

    elif [ "$timer" == "true" ]
    then
        python3 src/glouton.py $path false $timer

    else
        python3 src/glouton.py $path false false
    fi

#ALGO PROG DYNAMIQUE
elif [ $algo == "progdyn" ]
then
    if [ "$couple" == 'true' ] && [ "$timer" == 'true' ]
    then
        python3 src/progdyn.py $path $couple $timer

    elif [ "$couple" == "true" ]
    then
        python3 src/progdyn.py $path $couple false

    elif [ "$timer" == "true" ]
    then
        python3 src/progdyn.py $path false $timer

    else
        python3 src/progdyn.py $path false false
    fi

#ALGO SEUIL
elif [ $algo == "tabou" ]
then
    if [ "$couple" == 'true' ] && [ "$timer" == 'true' ]
    then
        python3 src/tabou.py $path $couple $timer

    elif [ "$couple" == "true" ]
    then
        python3 src/tabou.py $path $couple false

    elif [ "$timer" == "true" ]
    then
        python3 src/tabou.py $path false $timer

    else
        python3 src/tabou.py $path false false
    fi

#ERROR
else
    echo "Choisir un algo valide {glouton, progdyn, tabou}"
fi
