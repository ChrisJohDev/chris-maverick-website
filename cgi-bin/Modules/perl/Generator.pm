package Generator;

# ********File: Generator.pm********
# *******Version 1.001*******
# ******Company: Maverick Webdesign part of JOHANNESSON INFORMATION TECHNOLOGY******
# *****Author: Chris Johannesson******
# ****Copyright 2003 Maverick Webdesign****
#
# Description: This module generates HTML / XML code.
# Methods: genHtml(), genXml(), tableMaker()

#use strict;
use Exporter;
use CGI;
	
our @ISA = qw(Exporter);
our @EXPORT = qw(genHtml);



sub genHtml {

# *******Name: genHtml *******
# ******Version: 1.1******
# *****Company: Maverick Webdesign part of JOHANNESSON INFORMATION TECHNOLOGY*****
# ****Author: Chris Johannesson*****
# ***Copyright 2003 Maverick Webdesign***
#
# In:		@textFile (paths to the textfiles containing the content to be displayed)
#		$template (path to the HTML template to be used)
#
# Output:	Returns the whole HTML page to be displayed.
#

	my ($marker, $mark, $value, $wholeFile, $thisval, %valueof, $i, $index, $file);
	my (@textFile, $template, $pageTitle);
	my %temp2;
	my $temp=$_[0];
	$template=$_[1];
	
	@textFile=split(",", $temp);
	
	$index=$#textFile;
	
# Collect all data from all the text files.
	$i=0;
	while ($i<($index+1)){
	
		open(TEXTFILE, $textFile[$i]);

		while (<TEXTFILE>) {
			chomp($_);
			($marker, $value) = split("\t", $_);
			$valueof{$marker}=$value;
		}

		close(TEXTFILE);
		$i++;
	}

# Check if table in page.
	if ($valueof{'table'}) {
	$file="../public_html/temp/temp.html";
		open DATAFILE, "<$file";
	
	%temp2=tableMaker('1', $valueof{'table'});
		foreach (keys %temp2) {
			$valueof{$_}=join ('', <DATAFILE>);
		}
	delete $valueof{'table'}; # Deletes the table key and value.
	close DATAFILE;
	open EMPTYFILE, ">$file";
	print EMPTYFILE "";
	close EMPTYFILE;
	}
# Read in the NavBar.
	if ($valueof{'navbar:NAV001'}) {
		open NAVBAR, "$valueof{'navbar:NAV001'}";
		$valueof{'navbar:NAV001'}=join ('', <NAVBAR>);
		close NAVBAR;
	}



# Read in the html template.
	open(TMPLT, $template);

	$wholeFile=join ('', <TMPLT>);

	close TMPLT;

	foreach $mark (keys %valueof) {
		$thisval=$valueof{$mark};
		$wholeFile=~ s/$mark/$thisval/g;
	}
	


return $wholeFile;
}
1;

sub genXml {

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! NOT FUNCTIONAL !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# *******Name: genXml *******
# ******Version: 0.0******
# *****Company: Maverick Webdesign part of JOHANNESSON INFORMATION TECHNOLOGY*****
# ****Author: Chris Johannesson*****
# ***Copyright 2003 Maverick Webdesign***
#
# In:		
#
# Output:	Returns the whole XML page to be displayed.
#

}

sub tableMaker {

# *******Name: tableMaker *******
# ******Version: 0.0******
# *****Company: Maverick Webdesign part of JOHANNESSON INFORMATION TECHNOLOGY*****
# ****Author: Chris Johannesson*****
# ***Copyright 2003 Maverick Webdesign***
#
# In:		An array containing (numbOfTables, filepath to data)
#
# Output:	Returns all tables to be entered in to the <table></table> tags in the HTML document.
#
	my @input=@_;
	my ($i, $n, $numbTables, $table, $row, $column, $rowValue, @output, @a, $numberColumns, $numberRows, @mark, %rValue, $filePath, @temp);
our @rString;	
	
# Read from the source file and put in to a multi dimensional array
	$numbTables=1;

	while ($numbTables<($input[0]+1)) {
	
		$table=($numbTables-1);
		
		$filePath=$input[$numbTables];	

		open(TABLE1, "$filePath");
		$row=0;
		
		# Read each line as one string
		while (<TABLE1>) { 
			chomp($_);
			@a=split(';', $_); # Splits the row and assigns the values to @a
			
			$column=0;
				while ($a[$column] && $column<10) {
				
					$output[$row]->[$column]=$a[$column];
					$column++;
				}

			$row++;
		}

		close(TABLE1);


		# Number of columns in the file/table.
		$numberColumns=$column;
		# Number of rows in the file/table.
		$numberRows=$row;

my $file="../public_html/temp/temp.html";
		$row=0;
		
		while ($row < $numberRows) {
		open ROW1, ">>$file";
			print ROW1  "<tr>";
close ROW1;
			$column=0;
			open COLUMN1, ">>$file";
			while ($column < $numberColumns) {
				print COLUMN1 "<td>$output[$row][$column]</td>";
				$column++;
			}
			
close COLUMN1;

			open ROW2, ">>$file";
			print ROW2 "</tr>";
			
close ROW2;


			$row++;
		}
		
		$table++;
		if ($table>99) {
			$mark[$table]="table:TBL$table";
		} elsif ($numbTables>9) {
			$mark[$table]="table:TBL0$table";
		} else {
			$mark[$table]="table:TBL00$table";
		}
		open OUT, "$file";
		$rString=join('', <OUT>);
		$rValue{$mark[$table]} = $rString[$table];
		$numbTables++;
		close OUT;
	}
	
	return %rValue;
}



