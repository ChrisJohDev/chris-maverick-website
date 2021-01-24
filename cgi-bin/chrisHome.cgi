#!/usr/bin/perl -wT

#****** File: chrisHome.cgi******
# Created: April 8 2003
# Modified June 26 2003
#
# ******Creator: Maverick Webdesign part of JOHANNESSON INFORMATION TECHNOLOGY******
# *****Author: Chris Johannesson******
# ****Copyright 2003 Maverick Webdesign****
#

use CGI;
use lib "modules/perl/";
use warnings;
#use strict;
use Generator;

my $q=new CGI;
my $outPut;
my @passTextFile=("../public_html/data/textfiles/mainPage.src,", "../public_html/data/textfiles/chrisData_nn.src");
my $passTemplate="../public_html/lib/templates/html/chrisHome_nn.dwt";
my ($os, $browser, $browserVersion, $osVersion, $temp, @tmp);

if ($q->user_agent=~ /opera/i) {
	$browser="Opera";
	$browserVersion= int($');
	if ($browserVersion eq 0) {
		$temp=substr($', 1, (length($')-1));
		$browserVersion=int($temp);
	}
} elsif ($q->user_agent=~ /msie/i) {
	$browser="InternetExplorer";
	$browserVersion= int($');
	if ($browserVersion eq 0) {
		$temp=substr($', 1, (length($')-1));
		$browserVersion=int($temp);
	}
} elsif ($q->user_agent=~ /amaya/i) {
	$browser="Amaya";
	$browserVersion= int($');
	if ($browserVersion eq 0) {
		$temp=substr($', 1, (length($')-1));
		$browserVersion=int($temp);
	}
} elsif ($q->user_agent=~ /mozilla/i) {
	if ($q->user_agent=~ /netscape/i) {
		$browser="Netscape";
		$browserVersion= int($');
		if ($browserVersion eq 0) {
			$temp=substr($', 1, (length($')-1));
			$browserVersion=int($temp);
		}
	} else {
		$browser="Mozilla";
		$browserVersion= int($');
		if ($browserVersion eq 0) {
			$temp=substr($', 1, (length($')-1));
			$browserVersion=int($temp);
		}
	}
} else {
	$browser="Unknown";
}

if ($browser eq "Mozilla" || $browser eq "Netscape" || $browser eq "Opera"){
	@passTextFile=('../public_html/data/textfiles/mainPage.src,', '../public_html/data/textfiles/chrisData_nn.src');
	$passTemplate='../public_html/lib/templates/html/chrisHome_nn.dwt';

if ($q->param('sendData')) {
 	SWITCH: {
 		if ($q->param('sendData') == "0") {
 			@passTextFile=('../public_html/data/textfiles/mainPage.src,', '../public_html/data/textfiles/chrisData_nn.src');
			 $passTemplate='../public_html/lib/templates/html/chrisHome_nn.dwt';
			 last; };
 		if ($q->param('sendData') == "1") {
 			@passTextFile=('../public_html/data/textfiles/resumePage.src,', '../public_html/data/textfiles/chrisData_nn.src');
			 $passTemplate='../public_html/lib/templates/html/chrisResume_nn.dwt';
			 last;};
 		if ($q->param('sendData') == "2") { 
 			@passTextFile=('../public_html/data/textfiles/chrisDefaultPage.src,', '../public_html/data/textfiles/chrisData_nn.src');
			 $passTemplate='../public_html/lib/templates/html/chrisDefaultPage_nn.dwt';
 			last; };
 		if ($q->param('sendData') == "3") { 
 			@passTextFile=('../public_html/data/textfiles/chrisInfoPage.src,', '../public_html/data/textfiles/chrisData_nn.src');
			 $passTemplate='../public_html/lib/templates/html/chrisPage_nn.dwt';
 			last; };
 		if ($q->param('sendData') == "4") { 
 			@passTextFile=('../public_html/data/textfiles/downloadPageData.src,', '../public_html/data/textfiles/chrisData_nn.src');
			 $passTemplate='../public_html/lib/templates/html/chrisPage_nn.dwt';
 			last; };
 		if ($q->param('sendData') == "5") {
 			print $q->redirect("/cgi-bin/runMail.cgi");
			 last; };
 		if ($q->param('sendData') == "6") { 
 			@passTextFile=('../public_html/data/textfiles/chrisLinksPageData.src,', '../public_html/data/textfiles/chrisData_nn.src');
			 $passTemplate='../public_html/lib/templates/html/chrisPage_nn.dwt';
 			last; };
 	}
 }
 }elsif ($browser eq "InternetExplorer" || $browser eq "Unknown"){
	@passTextFile=('../public_html/data/textfiles/mainPage.src,', '../public_html/data/textfiles/chrisData_ie.src');
	$passTemplate='../public_html/lib/templates/html/chrisHome_ie.dwt';
 
 if ($q->param('sendData')) {
 	SWITCH: {
 		if ($q->param('sendData') == "0") {
 			@passTextFile=('../public_html/data/textfiles/mainPage.src,', '../public_html/data/textfiles/chrisData_ie.src');
			 $passTemplate='../public_html/lib/templates/html/chrisHome_ie.dwt';
			 last; };
 		if ($q->param('sendData') == "1") {
 			@passTextFile=('../public_html/data/textfiles/resumePage.src,', '../public_html/data/textfiles/chrisData_ie.src');
			 $passTemplate='../public_html/lib/templates/html/chrisResume.dwt';
			 last;};
 		if ($q->param('sendData') == "2") { 
 			@passTextFile=('../public_html/data/textfiles/chrisDefaultPage.src,', '../public_html/data/textfiles/chrisData_ie.src');
			 $passTemplate='../public_html/lib/templates/html/chrisDefaultPage.dwt';
 			last; };
 		if ($q->param('sendData') == "3") { 
 			@passTextFile=('../public_html/data/textfiles/chrisInfoPage.src,', '../public_html/data/textfiles/chrisData_ie.src');
			 $passTemplate='../public_html/lib/templates/html/chrisPage_ie.dwt';
 			last; };
 		if ($q->param('sendData') == "4") { 
 			@passTextFile=('../public_html/data/textfiles/downloadPageData.src,', '../public_html/data/textfiles/chrisData_ie.src');
			 $passTemplate='../public_html/lib/templates/html/chrisPage_ie.dwt';
 			last; };
 		if ($q->param('sendData') == "5") {
 			print $q->redirect("/cgi-bin/runMail.cgi");
			 last; };
 		if ($q->param('sendData') == "6") { 
 			@passTextFile=('../public_html/data/textfiles/chrisLinksPageData.src,', '../public_html/data/textfiles/chrisData_ie.src');
			 $passTemplate='../public_html/lib/templates/html/chrisPage_ie.dwt';
 			last; };
 	}
 }
 }
 
 	$outPut=genHtml("@passTextFile", "$passTemplate");


if ($outPut) {

print $q->header;	# Nessecary for the script to work in Netscape Navigator 4.74

print <<HTML;

$outPut

HTML

}

