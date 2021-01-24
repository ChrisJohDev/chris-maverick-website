#!/usr/bin/perl -wT

#****** File: runMail.cgi******
# Created: June 24 2003
#
# Modified: June 26 2003
#
# ******Creator: Maverick Webdesign part of JOHANNESSON INFORMATION TECHNOLOGY******
# *****Author: Chris Johannesson******
# ****Copyright 2003 Maverick Webdesign****
#

use strict;
use CGI;

BEGIN {
	$ENV{PATH} = "/bin:/usr/bin";
	delete @ENV{ qw( IFS CDPATH ENV BASH_ENV ) };
}

my $q = new CGI;
my $email = validate_email_address( $q->param( "sender_email" ) );
my $message = $q->param( "sender_message" );
my $name = $q->param("sender_name");
my $new_location = $q->param("go_to");
my $self = $q->url;

if ($q->param){

if ($new_location) {

print $q->redirect("$new_location");

} else {

unless ($name) {
	print	$q->header("text/html"),
			$q->start_html( -title=>"No Name", -bgcolor=>"#ff0000"),
			$q->h1("<center>No Name</center>"),
			$q->hr,
			$q->p(	"<center>The email you are trying to send contains no name." .
					"<br>Please, use your browser's back button to " .
					"return to the form and try again.</center>" );
			$q->end_html;
	exit;
}

unless ($email) {
	print	$q->header("text/html"),
			$q->start_html( -title=>"Invalid Email Address", -bgcolor=>"#ff0000"),
			$q->h1("<center>Invalid Email Address</center>"),
			$q->hr,
			$q->p(	"<center>The email address you have entered is invalid." .
					"<br>Please, use your browser's back button to " .
					"return to the form and try again.</center>" );
			$q->end_html;
	exit;
}

unless ($message) {
	print	$q->header("text/html"),
			$q->start_html( -title=>"No Message", -bgcolor=>"#ff0000"),
			$q->h1("<center>No Message</center>"),
			$q->hr,
			$q->p(	"<center>The email you are trying to send contains no message." .
					"<br>Please, use your browser's back button to " .
					"return to the form and try again.</center>" );
			$q->end_html;
	exit;
}

send_feedback($email, $name, $message);
send_reciept($email, $message);
confirmation($email, $name, $message);

#print $q->redirect("/cgi-bin/chrisHome.cgi"); Can't be used without causing an 302 error server side.
}
}else {

print $q->header;	# Nessecary for the script to work in Netscape Navigator

	print <<FORM;

<html>
	<head><title>Contact Chris</title>
	<style type="text/css" media="screen"><!--
#mainTable     { position: absolute; top: 179px; left: 157px; width: 312px; height: 188px; visibility: visible; display: block }
#controlTable       { position: absolute; top: 428px; left: 218px; width: 203px; height: 50px; visibility: visible; display: block }
#input { background-color: #dcdcdc }
--></style>
	</head>
	<body bgcolor="#0000ff">
		<center><u><h1>Contact Form</h1></u><p>
		There will be an automated confirmation receipt sent to your email address.<br>I will contact you as soon as possible.<br />Depending on where I am it might take a few days but I will get back to you.</p></center>
		<hr /><br />
		<form action="$self" method="post">
			<div id="mainTable">
			<table>
				<tr>
					<td>Your name: </td>
					<td><input id="input" type="text" size="25" name="sender_name"  /></td>
				</tr>
				<tr>
					<td>Your email address: </td>
					<td><input id="input" type="text" size="25" name="sender_email"></td>
				</tr>
			</table>
			<table>
				<tr>
					<td>Enter your message here:<br /><textarea id="input" name="sender_message" rows="7" cols="47"></textarea></td>
				</tr>
			</table>
			
			</div>
			
			<div id="controlTable">
				<table>
					<tr>
						<td><input type="reset" name="Reset" /></td>
						<td colspan="30"></td>
						<td><input type="submit" name="submit" value="Send email"/></td>
					</tr>
				</table>
			</div>
		</form>
	</body>
</html>
FORM

}
		

sub confirmation {
	my ($email, $name, $message) = @_;
	my $q = new CGI;
	my $self = $q->url;

print $q->header;	# Nessecary for the script to work in Netscape Navigator

print <<HTML;

<html><head><title>Confirmtion for $name</title></head>
<body bgcolor="#0000ff">
<center><h1>Confirmation</h1></center><hr /><br />
<center><p>Thank you $name for contacting me</p>
<p>Your message:<br />$message<br /><br />Has been delivered and a receipt has been sent to: $email</p>
<p>If appropriate I will respond to your email shortly.<br /><br />Sincerely yours,<br />Chris Johannesson</p><hr /></center>
<form action="$self" name="return">
<input type="hidden" name="go_to" value="/cgi-bin/chrisHome.cgi">
<center><input type="submit" name="return" value="Return" /></center></form>
</body></html>

HTML

}

sub send_feedback {

	my ($email, $name, $message) = @_;
	
	open (MAIL, '|/usr/sbin/sendmail -oi -t') || die "Could not open send_feedback sendmail: $!";
	
	print MAIL <<END_OF_MESSAGE;
From: $email;
To: cj\@maverick-web.com
Reply-To: $email
Subject: CONTACT ME from chris web site

Message from:
$name	$email


$message

END_OF_MESSAGE

	close MAIL or die "Could not close send_feedback sendmail: $!";
}

sub send_reciept {

	my ($to_email, $message) = @_;
	my $from_email = "donotreply\@maverick-web.com";
	my $from_name = "Do NOT Reply";
	
	open (MAIL, '|/usr/sbin/sendmail -oi -t') || die "Could not open sendmail: $!";
	
	print MAIL <<END_OF_MESSAGE;
From: maverick\@maverick-web.com;
Reply-To: donotreply\@maverick-web.com
To: $to_email
Subject: Do NOT Reply (Your confirmation)

*****DO NOT REPLY*****

This is an automated reply.
Your message has been sent and I will be responding to you shortly.

Regards,
Chris Johannesson

Visit my FRIENDS forum on http://www.maverick-web.com/friends


Your message:

$message

END_OF_MESSAGE

	close MAIL || die "Could not close send_reciept sendmail: $!";
}

sub validate_email_address {
#
# Source: CGI Programming 2nd Edition p. 219-220 by S. Guelish, S. Gundavaram & G. Birznieks on O'Reill books.
# 
# Continue the work on validating email address and include a set that will detect
# spaces within elements as they are illigal.
#
# Remember the approach / method of building the final Regular Expression.
#
# Name:	validate_email_address
#
# Input:		Any email address to check (string)
# Output:	The submitted email address (with all spaces stripped i.e. without spaces) or
#			an empty string which evaluates to false in Perl.
#
	my $address_to_check = shift;
	$address_to_check =~ s/("(?:[^"\\]|\\.)*"|[^\t "]*)[ \t]*/$1/g;
	
	my $esc			= '\\\\';
	my $space			= '\040';
	my $ctrl				= '\000-\037';
	my $dot				= '\.';
	my $nonASCII		= '\x80-\xff';
	my $CRlist			= '\012\015';
	my $letter			= 'a-zA-Z';
	my $digit			= '\d';
	my $atom_char		= qq{ [^$space<>\@,;:".\\[\\]$esc$ctrl$nonASCII] };
	my $atom			= qq{ $atom_char+ };
	my $byte			= qq{ (?:	1?$digit?$digit	|
									2[0-4]$digit		|
									25[0-5]			) };
	my $qtext			= qq{ [^$esc$nonASCII$CRlist"] };
	my $quoted_pair	= qq{ $esc [^$nonASCII] };
	my $quoted_str		= qq{ " (?: $qtext | $quoted_pair )* " };
	my $word			= qq{ (?: $atom | $quoted_str ) };
	my $ip_address		= qq{ \\[ $byte (?: $dot $byte ) {3} \\] };
	my $sub_domain	= qq{	[$letter$digit]
								[$letter$digit-]{0,61} [$letter$digit]};
	my $top_level		= qq{ (?: $atom_char ){2,4} };
	my $domain_name	= qq{ (?: $sub_domain $dot )+ $top_level };
	my $domain			= qq{ (?: $domain_name | $ip_address ) };
	my $local_part		= qq{ $word (?: $dot $word )* };
	my $address		= qq{ $local_part \@ $domain };
	
	return $address_to_check =~ /^$address$/ox ? $address_to_check : "";
}

