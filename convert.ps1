Get-ChildItem ".\machine-learning-python\machine-learning-chapter-18\assets" -Filter *.py | 
Foreach-Object {
    $fileName = $_.FullName
	$outFileName= $fileName.Replace('.py', '') + '.ipynb'
	
	ipynb-py-convert $fileName $outFileName 
	
	echo $outFileName
}