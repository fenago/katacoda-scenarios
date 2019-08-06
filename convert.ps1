Get-ChildItem ".\machine-learning-chapter-12\assets" -Filter *.py | 
Foreach-Object {
    $fileName = $_.FullName
	$outFileName= $fileName.Replace('.py', '') + '.ipynb'
	
	ipynb-py-convert $fileName $outFileName 
	
	echo $outFileName
}