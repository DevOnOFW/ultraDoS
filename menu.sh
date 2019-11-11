PS3='Please enter your choice: '
echo "                           "
options=("IP Finder" "DDoS" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "IP Finder")
            echo -e "\e[32m "you chose Ip Finder" \e[0m"
python2 IPFINDER.py
            ;;
        "DDoS")
            echo -e "\e[32m "you chose DDoS"  \e[0m"
python2 DDOS.py
            ;;
        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done


