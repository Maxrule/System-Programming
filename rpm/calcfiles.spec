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
echo "Contents of temp_dir after unzip:"
ls -l temp_dir
cd temp_dir/System-Programming-main/ || { echo "Directory not found"; exit 1; }

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 %{_builddir}/System-Programming-main/calcfiless.sh %{buildroot}/usr/bin/calcfiless

%files
/usr/bin/calcfiless

%changelog
* Sun Sep 22 2024 Kovgan Maxim <maxim.kov4@gmail.com> - 1.0-1
- Initial build
