Name:           ffmpegthumbnailer
Version:        2.2.0
Release:        9%{?dist}
Summary:        Lightweight video thumbnailer that can be used by file managers

License:        GPLv2+
URL:            http://code.google.com/p/ffmpegthumbnailer/
Source0:        https://github.com/dirkvdb/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ffmpeg-devel, libpng-devel, libjpeg-devel
BuildRequires:  chrpath, cmake3, gcc-c++
%{?el7:BuildRequires: epel-rpm-macros}


%description
This video thumbnailer can be used to create thumbnails for your video files.

%package devel
Summary:        Headers and libraries for building apps that use ffmpegthumbnailer
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This video thumbnailer can be used to create thumbnails for your video files,
development package.

%prep
%setup -q
chmod -x README INSTALL COPYING AUTHORS

%build
%cmake3 -DENABLE_GIO=ON -DENABLE_THUMBNAILER=ON .

%make_build

 
%install
%make_install
#chrpath --delete $RPM_BUILD_ROOT%%{_bindir}/ffmpegthumbnailer
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%doc README AUTHORS
%license COPYING
%{_bindir}/ffmpegthumbnailer
%{_libdir}/libffmpegthumbnailer.so.4*
%{_mandir}/man1/ffmpegthumbnailer.1.gz
# gnome thumbnailer registration
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/ffmpegthumbnailer.thumbnailer

%files devel
%{_libdir}/libffmpegthumbnailer.so
%{_libdir}/pkgconfig/libffmpegthumbnailer.pc
%{_includedir}/libffmpegthumbnailer/


%changelog
* Tue Aug 06 2019 Leigh Scott <leigh123linux@gmail.com> - 2.2.0-9
- Rebuild for new ffmpeg version

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 08 2018 Antonio Trande <sagitter@fedoraproject.org> - 2.2.0-7
- Rebuild for ffmpeg-3.4.5 on el7
- Use ldconfig_scriptlets
- Use CMake3

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.2.0-5
- Rebuilt for new ffmpeg snapshot

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 2.2.0-3
- Rebuilt for ffmpeg-3.5 git

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 11 2017 Sérgio Basto <sergio@serjux.com> - 2.2.0-1
- Update ffmpegthumbnailer to 2.2.0

* Sat Apr 29 2017 Leigh Scott <leigh123linux@googlemail.com> - 2.1.2-3
- Rebuild for ffmpeg update

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 24 2016 Sérgio Basto <sergio@serjux.com> - 2.1.2-1
- Update ffmpegthumbnailer to 2.1.2
- Clean up spec, add license tag.
- Fix changelog dates.

* Sat Jul 30 2016 Julian Sikorski <belegdol@fedoraproject.org> - 2.1.1-2
- Rebuilt for ffmpeg-3.1.1

* Sat Jun 25 2016 Leigh Scott <leigh123linux@googlemail.com> - 2.1.1-1
- 2.1.1

* Thu Apr 09 2015 Magnus Tuominen <magnus.tuominen@gmail.com> - 2.0.9-1
- 2.0.9

* Sun Oct 19 2014 Sérgio Basto <sergio@serjux.com> - 2.0.8-11
- Rebuilt for FFmpeg 2.4.3

* Fri Sep 26 2014 Nicolas Chauvet <kwizart@gmail.com> - 2.0.8-10
- Rebuilt for FFmpeg 2.4.x

* Thu Aug 07 2014 Sérgio Basto <sergio@serjux.com> - 2.0.8-9
- Rebuilt for ffmpeg-2.3

* Sat Mar 29 2014 Sérgio Basto <sergio@serjux.com> - 2.0.8-8
- Rebuilt for ffmpeg-2.2

* Wed Nov 27 2013 Leigh Scott <leigh123linux@googlemail.com> - 2.0.8-7
- fix compile error

* Wed Oct 02 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.0.8-6
- Rebuilt

* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.0.8-5
- Rebuilt for FFmpeg 2.0.x

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.0.8-4
- Rebuilt for x264/FFmpeg

* Mon Mar 04 2013 Nicolas Chauvet <kwizart@gmail.com> - 2.0.8-3
- Rebuilt for F-19 Features

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.8-2
- Rebuilt for FFmpeg 1.0

* Wed Aug 29 2012 Magnus Tuominen <magnus.tuominen@gmail.com> - 2.0.8-1
- 2.0.8

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.7-4
- Rebuilt for c++ ABI breakage

* Tue Feb 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.7-3
- Rebuilt for x264/FFmpeg

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 2.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 29 2011 Magnus Tuominen <magnus.tuominen@gmail.com> - 2.0.7-1
- new version
- patches merged upstream

* Mon Sep 26 2011 Nicolas Chauvet <kwizart@gmail.com> - 2.0.6-3
- Rebuilt for FFmpeg-0.8*

* Sun Feb 13 2011 Magnus Tuominen <magnus.tuominen@gmail.com> - 2.0.6-2
- patch NULL reference to make rawhide build

* Fri Feb 04 2011 Magnus Tuominen <magnus.tuominen@gmail.com> - 2.0.6-1
- version bump
- patch libdl link issue
- add BR: automake and autoconf

* Sun Dec 05 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 2.0.5-1
- version bump
- enable gio-support

* Sat Aug 21 2010 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 2.0.4-2
- rebuilt

* Wed Aug 18 2010 Magnus Tuominen <magnus.tuominen@gmail.com> 2.0.4-1
- version bump

* Sun May 16 2010 Magnus Tuominen <magnus.tuominen@gmail.com> 2.0.2-1
- version bump

* Mon Apr 19 2010 Magnus Tuominen <magnus.tuominen@gmail.com> 2.0.1-1
- version bump
- libspatch.patch merged upstream, issue 59

* Mon Apr 12 2010 Magnus Tuominen <magnus.tuominen@gmail.com> 2.0.0-3
- drop _kde4_ macros
- moving chmod to %%prep
- moving %%{_includedir}/libffmpegthumbnailer to -devel
- track sonames closer
- license change to GPLv2+
- remove duplicate docs from -devel
- patching libs in pkgconfig%%{name}.pc, thanks to rdieter

* Sun Apr 11 2010 leigh scott <leigh123linux@googlemail.com> 2.0.0-2
- fix rpath
- enable jpeg and png support
- clean up spec file
- remove static libs as they aren't needed
- add docs

* Sat Apr 10 2010 Magnus Tuominen <magnus.tuominen@gmail.com> 2.0.0-1
- initial build
- has to be built with "QA_RPATHS=$[0x0001|0x0010 ]" for now
