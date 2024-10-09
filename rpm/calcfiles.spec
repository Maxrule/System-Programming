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
# Распаковка исходного архива
unzip -q %{SOURCE0}
cd System-Programming-main/

# Удаление символов возврата каретки (CRLF) из файлов
find . -type f -exec sed -i 's/\r$//g' {} \;

%install
# Создание директории для бинарного файла
mkdir -p %{buildroot}/usr/bin

# Установка скрипта в системный каталог
install -m 755 calcfiless.sh %{buildroot}/usr/bin/calcfiless

%files
/usr/bin/calcfiless

%changelog
* Wed Oct 09 2024 Kovgan Maxim <maxim.kov4@gmail.com> - 1.0-1
- Initial build
