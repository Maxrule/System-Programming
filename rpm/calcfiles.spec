Name:           calcfiles
Version:        1.0
Release:        1%{?dist}
Summary:        A simple script to calculate files in a directory
Requires:       unzip

License:        MIT
URL:            https://github.com/men325/System-Programming
Source0:        https://github.com/men325/System-Programming/archive/main.zip

BuildArch:      noarch

%description
calc_files.sh is a simple script that calculates the number of files in a directory.

%prep
unzip %SOURCE0
cd System-Programming-main/

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 %{_builddir}/System-Programming-main/calc_files.sh %{buildroot}/usr/bin/calc_files

%files
/usr/bin/calc_files

%changelog
* Sun Sep 22 2024 Kovgan Maxim <maxim.kov4@gmail.com> - 1.0-1
- Initial build