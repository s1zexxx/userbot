#!/bin/bash
print_center(){
    local x
    local y
    text="$*"
    x=$(( ($(tput cols) - ${#text}) / 2))
    echo -ne "\E[6n";read -sdR y; y=$(echo -ne "${y#*[}" | cut -d';' -f1)
    echo -ne "\033[${y};${x}f$*"
}

run_in_bg() {
    eval "$@" &>/dev/null & disown;
}

echo -e "\033[0;96mInstalling s1zex... Just a Moment...\033[0m"

eval "cd ~/ &&
rm -rf userbot &&
git clone --branch main https://github.com/s1zexxx/userbot &&
cd Netfoll &&
pip install -U pip &&
pip install -r requirements.txt &&
echo '' > ~/../usr/etc/motd &&
echo 'clear && . <(wget -qO- https://github.com/s1zexxx/userbot/assets/banner.sh) && cd ~/userbot && python3 -m s1zex --port 1242' > ~/.bash_profile"

echo -e "\033[0;96mStarting s1zex...\033[0m"

run_in_bg "python3 -m s1zex --port 1242"
sleep 10

echo -ne "\\033[2J\033[3;1f"
print_center "
\033[95ms1zex s1zex s1zex s1zex s1zex \033[0m
\033[95ms1zex s1zex s1zex s1zex s1zex \033[0m
\033[95ms1zex s1zex s1zex s1zex s1zex \033[0m
\033[95ms1zex s1zex s1zex s1zex s1zex \033[0m
\033[95ms1zex s1zex s1zex s1zex s1zex \033[0m

\033[95ms1zex loaded successfully!\033[0m
\033[95mWeb url: http://localhost:1242\033[0m
"

eval "termux-open-url http://localhost:1242"


