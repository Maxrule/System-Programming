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
unzip -o -O UTF-8 %{SOURCE0} -d temp_dir
echo "Contents of temp_dir/System-Programming-main:"
ls -l temp_dir/System-Programming-main/
if [ -d temp_dir/System-Programming-main ]; then
    echo "Directory exists."
else
    echo "Directory does not exist."
fi
sed -i 's/\r$//g' temp_dir/System-Programming-main/calcfiless.sh  # Уберите ^M
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
