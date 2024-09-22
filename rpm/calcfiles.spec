Name:           calcfiles
Version:        1.0
Release:        1%{?dist}
Summary:        A simple script to calculate files in a directory
Requires:       unzip

License:        MIT
URL:            https://github.com/Maxrule/System-Programming
Source0:        https://github.com/Maxrule/System-Programming/archive/main.zip

BuildArch:      noarch

%description
calcfiless.sh is a simple script that calculates the number of files in a directory.

%prep
unzip -o %{SOURCE0} -d temp_dir
ls -l temp_dir/System-Programming-main/  # Отображаем содержимое директории
sed -i 's/\r$//g' temp_dir/System-Programming-main/calcfiless.sh  # Уберите ^M
if [ ! -s temp_dir/System-Programming-main/calcfiless.sh ]; then
    echo "calcfiless.sh is empty or does not exist!"
    exit 1
fi
mv temp_dir/System-Programming-main/calcfiless.sh ./
rm -rf temp_dir

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 calcfiless.sh %{buildroot}/usr/bin/calcfiless

%files
/usr/bin/calcfiless

%changelog
* Sun Sep 22 2024 Kovgan Maxim <maxim.kov4@gmail.com> - 1.0-1
- Initial build
