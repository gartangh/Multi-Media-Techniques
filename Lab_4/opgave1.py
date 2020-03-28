import os
import subprocess

OriginalVideo = "PartyScene_416x240_25fps.yuv"
OriginalVideoPath = "YUV-bestanden/PartyScene_416x240_25fps.yuv"

# Open bestand
FilePath = os.path.join('YUV-bestanden', OriginalVideo)
print FilePath
# Bestandsgrootte
FileSize = os.path.getsize(FilePath)
print "Filesize = " + str(FileSize)

def config1():
	config = 1
	configPath = os.path.join('Opgave1', 'config'+ str(config) + '.csv')

	for q in xrange(1,52,5):
		print "config_" + str(config) + ", Q = " + str(q)

		CodedVideo = "Coded/coded_" + str(config) + "_" + str(q) + ".264"
		# x264.exe -q [quantisatieparameter] -v -o [output].264 --tune psnr --fps 25 --frames 50 --input-res 416x240 --keyint 1 --min-keyint 1 --b-adapt 0 [sequentie].yuv
		args=["uitvoerbare_bestanden/x264.exe", "-q", str(q), "-v", "-o", CodedVideo, "--tune", "psnr", "--fps", "25", "--frames", "50", "--input-res", "416x240", "--keyint", "1", "--min-keyint", "1",  "--b-adapt", "0", OriginalVideoPath]
		outFile = open('Out/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		DecodedVideo = "Decoded/decoded_" + str(config) + "_" + str(q) + ".yuv"
		# avcdecoder.exe -i [input].264 -o [output_dec].yuv
		args=["uitvoerbare_bestanden/avcdecoder.exe", "-i", CodedVideo, "-o", DecodedVideo]
		outFile = open('Out/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		PSNRFile = "PSNR/psnr_" + str(config) + "_" + str(q)
		# VQMT.exe [OriginalVideo] [ProcessedVideo] [Height] [Width] [Frames] [ChromaFormat] [Output] [Metrics]
		args=["uitvoerbare_bestanden/VQMT.exe", FilePath, DecodedVideo, "240", "416", "50", "YUV420", PSNRFile, "PSNR"]
		outFile = open('Out/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		AveragePSNR = [x for x in open(PSNRFile + "_psnr.csv", 'r').readlines() if "average" in x][0].split(',')[1]
		print "AveragePSNR = " + str(AveragePSNR)
		
		configFile = open(configPath, 'a')
		configFile.write(str(q) + "," + str(os.path.getsize(CodedVideo)) + "," + str(AveragePSNR) + '\n')
		configFile.close()


def config2():
	config = 2
	configPath = os.path.join('Opgave1', 'config'+ str(config) + '.csv')

	for q in xrange(1,52,5):
		print "config_" + str(config) + ", Q = " + str(q)

		CodedVideo = "Coded/coded_" + str(config) + "_" + str(q) + ".264"
		# x264.exe -q [quantisatieparameter] -v -o [output].264 --tune psnr --fps 25 --frames 50 --input-res 416x240 --keyint 16 --min-keyint 16 --bframe 0 --b-adapt 0 [sequentie].yuv
		args=["uitvoerbare_bestanden/x264.exe", "-q", str(q), "-v", "-o", CodedVideo, "--tune", "psnr", "--fps", "25", "--frames", "50", "--input-res", "416x240", "--keyint", "16", "--min-keyint", "16", "--bframe", "0", "--b-adapt", "0", OriginalVideoPath]
		outFile = open('Out/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		DecodedVideo = "Decoded/decoded_" + str(config) + "_" + str(q) + ".yuv"
		# avcdecoder.exe -i [input].264 -o [output_dec].yuv
		args=["uitvoerbare_bestanden/avcdecoder.exe", "-i", CodedVideo, "-o", DecodedVideo]
		outFile = open('Out/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		PSNRFile = "PSNR/psnr_" + str(config) + "_" + str(q)
		# VQMT.exe [OriginalVideo] [ProcessedVideo] [Height] [Width] [Frames] [ChromaFormat] [Output] [Metrics]
		args=["uitvoerbare_bestanden/VQMT.exe", FilePath, DecodedVideo, "240", "416", "50", "YUV420", PSNRFile, "PSNR"]
		outFile = open('Out/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		AveragePSNR = [x for x in open(PSNRFile + "_psnr.csv", 'r').readlines() if "average" in x][0].split(',')[1]
		print "AveragePSNR = " + str(AveragePSNR)
		
		configFile = open(configPath, 'a')
		configFile.write(str(q) + "," + str(os.path.getsize(CodedVideo)) + "," + str(AveragePSNR) + '\n')
		configFile.close()

def config3():
	config = 3
	configPath = os.path.join('Opgave1', 'config'+ str(config) + '.csv')

	for q in xrange(1,52,5):
		print "config_" + str(config) + ", Q = " + str(q)

		CodedVideo = "Coded/coded_" + str(config) + "_" + str(q) + ".264"
		# x264.exe -q [quantisatieparameter] -v -o [output].264 --tune psnr --fps 25 --frames 50 --input-res 416x240  --keyint 16 --min-keyint 16 --bframe 4 --b-adapt 0 [sequentie].yuv
		args=["uitvoerbare_bestanden/x264.exe", "-q", str(q), "-v", "-o", CodedVideo, "--tune", "psnr", "--fps", "25", "--frames", "50", "--input-res", "416x240", "--keyint", "16", "--min-keyint", "16", "--bframe", "4", "--b-adapt", "0", OriginalVideoPath]
		outFile = open('Out/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		DecodedVideo = "Decoded/decoded_" + str(config) + "_" + str(q) + ".yuv"
		# avcdecoder.exe -i [input].264 -o [output_dec].yuv
		args=["uitvoerbare_bestanden/avcdecoder.exe", "-i", CodedVideo, "-o", DecodedVideo]
		outFile = open('Out/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		PSNRFile = "PSNR/psnr_" + str(config) + "_" + str(q)
		# VQMT.exe [OriginalVideo] [ProcessedVideo] [Height] [Width] [Frames] [ChromaFormat] [Output] [Metrics]
		args=["uitvoerbare_bestanden/VQMT.exe", FilePath, DecodedVideo, "240", "416", "50", "YUV420", PSNRFile, "PSNR"]
		outFile = open('Out/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		AveragePSNR = [x for x in open(PSNRFile + "_psnr.csv", 'r').readlines() if "average" in x][0].split(',')[1]
		print "AveragePSNR = " + str(AveragePSNR)
		
		configFile = open(configPath, 'a')
		configFile.write(str(q) + "," + str(os.path.getsize(CodedVideo)) + "," +  str(AveragePSNR) + '\n')
		configFile.close()

def config4():
	config = 4
	configPath = os.path.join('Opgave1', 'config'+ str(config) + '.csv')

	for q in xrange(1,52,5):
		print "config_" + str(config) + ", Q = " + str(q)

		CodedVideo = "Coded/coded_" + str(config) + "_" + str(q) + ".264"
		# x264.exe -q [quantisatieparameter] -v -o [output].264 --tune psnr --fps 25 --frames 50 --input-res 416x240  --keyint 16 --min-keyint 16 --bframe 4 --b-adapt 0 --subme 0 --partitions none [sequentie].yuv
		args=["uitvoerbare_bestanden/x264.exe", "-q", str(q), "-v", "-o", CodedVideo, "--tune", "psnr", "--fps", "25", "--frames", "50", "--input-res", "416x240", "--keyint", "16", "--min-keyint", "16", "--bframe", "4", "--b-adapt", "0", "--subme", "0", "--partitions", "none", OriginalVideoPath]
		outFile = open('Out/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		DecodedVideo = "Decoded/decoded_" + str(config) + "_" + str(q) + ".yuv"
		# avcdecoder.exe -i [input].264 -o [output_dec].yuv
		args=["uitvoerbare_bestanden/avcdecoder.exe", "-i", CodedVideo, "-o", DecodedVideo]
		outFile = open('Out/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		PSNRFile = "PSNR/psnr_" + str(config) + "_" + str(q)
		# VQMT.exe [OriginalVideo] [ProcessedVideo] [Height] [Width] [Frames] [ChromaFormat] [Output] [Metrics]
		args=["uitvoerbare_bestanden/VQMT.exe", FilePath, DecodedVideo, "240", "416", "50", "YUV420", PSNRFile, "PSNR"]
		outFile = open('Out/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		AveragePSNR = [x for x in open(PSNRFile + "_psnr.csv", 'r').readlines() if "average" in x][0].split(',')[1]
		print "AveragePSNR = " + str(AveragePSNR)
		
		configFile = open(configPath, 'a')
		configFile.write(str(q) + "," + str(os.path.getsize(CodedVideo)) + "," +  str(AveragePSNR) + '\n')
		configFile.close()

def config5():
	config = 5
	configPath = os.path.join('Opgave1', 'config'+ str(config) + '.csv')

	for q in xrange(1,52,5):
		print "config_" + str(config) + ", Q = " + str(q)

		CodedVideo = "Coded/coded_" + str(config) + "_" + str(q) + ".264"
		# x264.exe -q [quantisatieparameter] -v -o [output].264 --tune psnr --fps 25 --frames 50 --input-res 416x240  --keyint 16 --min-keyint 16 --bframe 4 --b-adapt 0 --subme 11 --partitions all [sequentie].yuv
		args=["uitvoerbare_bestanden/x264.exe", "-q", str(q), "-v", "-o", CodedVideo, "--tune", "psnr", "--fps", "25", "--frames", "50", "--input-res", "416x240", "--keyint", "16", "--min-keyint", "16", "--bframe", "4", "--b-adapt", "0", "--subme", "11", "--partitions", "all", OriginalVideoPath]
		outFile = open('Out/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		DecodedVideo = "Decoded/decoded_" + str(config) + "_" + str(q) + ".yuv"
		# avcdecoder.exe -i [input].264 -o [output_dec].yuv
		args=["uitvoerbare_bestanden/avcdecoder.exe", "-i", CodedVideo, "-o", DecodedVideo]
		outFile = open('Out/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		PSNRFile = "PSNR/psnr_" + str(config) + "_" + str(q)
		# VQMT.exe [OriginalVideo] [ProcessedVideo] [Height] [Width] [Frames] [ChromaFormat] [Output] [Metrics]
		args=["uitvoerbare_bestanden/VQMT.exe", FilePath, DecodedVideo, "240", "416", "50", "YUV420", PSNRFile, "PSNR"]
		outFile = open('Out/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		AveragePSNR = [x for x in open(PSNRFile + "_psnr.csv", 'r').readlines() if "average" in x][0].split(',')[1]
		print "AveragePSNR = " + str(AveragePSNR)
		
		configFile = open(configPath, 'a')
		configFile.write(str(q) + "," + str(os.path.getsize(CodedVideo)) + "," +  str(AveragePSNR) + '\n')
		configFile.close()

def config6():
	config = 6
	configPath = os.path.join('Opgave1', 'config'+ str(config) + '.csv')

	for q in xrange(1,52,5):
		print "config_" + str(config) + ", Q = " + str(q)

		CodedVideo = "Coded/coded_" + str(config) + "_" + str(q) + ".264"
		# x264.exe -q [quantisatieparameter] -v -o [output].264 --tune psnr --fps 25 --frames 50 --input-res 416x240  --keyint 16 --min-keyint 16 --bframe 4 --b-adapt 0 --me tesa --subme 11 --partitions all [sequentie].yuv
		args=["uitvoerbare_bestanden/x264.exe", "-q", str(q), "-v", "-o", CodedVideo, "--tune", "psnr", "--fps", "25", "--frames", "50", "--input-res", "416x240", "--keyint", "16", "--min-keyint", "16", "--bframe", "4", "--b-adapt", "0", "--me", "tesa", "--subme", "11", "--partitions", "all", OriginalVideoPath]
		outFile = open('Out/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		DecodedVideo = "Decoded/decoded_" + str(config) + "_" + str(q) + ".yuv"
		# avcdecoder.exe -i [input].264 -o [output_dec].yuv
		args=["uitvoerbare_bestanden/avcdecoder.exe", "-i", CodedVideo, "-o", DecodedVideo]
		outFile = open('Out/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		PSNRFile = "PSNR/psnr_" + str(config) + "_" + str(q)
		# VQMT.exe [OriginalVideo] [ProcessedVideo] [Height] [Width] [Frames] [ChromaFormat] [Output] [Metrics]
		args=["uitvoerbare_bestanden/VQMT.exe", FilePath, DecodedVideo, "240", "416", "50", "YUV420", PSNRFile, "PSNR"]
		outFile = open('Out/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		AveragePSNR = [x for x in open(PSNRFile + "_psnr.csv", 'r').readlines() if "average" in x][0].split(',')[1]
		print "AveragePSNR = " + str(AveragePSNR)
		
		configFile = open(configPath, 'a')
		configFile.write(str(q) + "," + str(os.path.getsize(CodedVideo)) + "," +  str(AveragePSNR) + '\n')
		configFile.close()

def config7():
	config = 7
	configPath = os.path.join('Opgave1', 'config'+ str(config) + '.csv')

	for q in xrange(1,52,5):
		print "config_" + str(config) + ", Q = " + str(q)

		CodedVideo = "Coded/coded_" + str(config) + "_" + str(q) + ".264"
		# x264.exe -q [quantisatieparameter] -v -o [output].264 --tune psnr --fps 25 --frames 50 --input-res 416x240  --keyint 16 --min-keyint 16 --bframe 4 --b-adapt 0 --me dia --subme 0 --partitions all [sequentie].yuv
		args=["uitvoerbare_bestanden/x264.exe", "-q", str(q), "-v", "-o", CodedVideo, "--tune", "psnr", "--fps", "25", "--frames", "50", "--input-res", "416x240", "--keyint", "16", "--min-keyint", "16", "--bframe", "4", "--b-adapt", "0", "--me", "dia", "--subme", "0", "--partitions", "all", OriginalVideoPath]
		outFile = open('Out/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		DecodedVideo = "Decoded/decoded_" + str(config) + "_" + str(q) + ".yuv"
		# avcdecoder.exe -i [input].264 -o [output_dec].yuv
		args=["uitvoerbare_bestanden/avcdecoder.exe", "-i", CodedVideo, "-o", DecodedVideo]
		outFile = open('Out/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		PSNRFile = "PSNR/psnr_" + str(config) + "_" + str(q)
		# VQMT.exe [OriginalVideo] [ProcessedVideo] [Height] [Width] [Frames] [ChromaFormat] [Output] [Metrics]
		args=["uitvoerbare_bestanden/VQMT.exe", FilePath, DecodedVideo, "240", "416", "50", "YUV420", PSNRFile, "PSNR"]
		outFile = open('Out/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		AveragePSNR = [x for x in open(PSNRFile + "_psnr.csv", 'r').readlines() if "average" in x][0].split(',')[1]
		print "AveragePSNR = " + str(AveragePSNR)
		
		configFile = open(configPath, 'a')
		configFile.write(str(q) + "," + str(os.path.getsize(CodedVideo)) + "," +  str(AveragePSNR) + '\n')
		configFile.close()

def config8():
	config = 8
	configPath = os.path.join('Opgave1', 'config'+ str(config) + '.csv')

	for q in [1766225,1342400,934800,617700,373950,205375,111425,56975,27950,13750,7525]:
		print "config_" + str(config) + ", Q = " + str(q)

		CodedVideo = "Coded/coded_" + str(config) + "_" + str(q) + ".264"
		# x264.exe -B B/1000  -v -o [output].264 --nal-hrd cbr --vbv-maxrate B/1000 --vbv-bufsize B/25000 --tune psnr --fps 25 --frames 50 --input-res 416x240 --keyint 16 --min-keyint 16 --bframe 0 --b-adapt 0 [sequentie].yuv
		args=["uitvoerbare_bestanden/x264.exe", "-B", str(q/1000), "-v", "-o", CodedVideo, "--nal-hrd", "cbr", "--vbv-maxrate",str(q/1000),"--vbv-bufsize", str(q/25000), "--tune", "psnr", "--fps", "25", "--frames", "50", "--input-res", "416x240", "--keyint", "16", "--min-keyint", "16", "--bframe", "0", "--b-adapt", "0", OriginalVideoPath]
		outFile = open('Out/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]

		outFile.close()
		errFile.close()

		DecodedVideo = "Decoded/decoded_" + str(config) + "_" + str(q) + ".yuv"
		# avcdecoder.exe -i [input].264 -o [output_dec].yuv
		args=["uitvoerbare_bestanden/avcdecoder.exe", "-i", CodedVideo, "-o", DecodedVideo]
		outFile = open('Out/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		PSNRFile = "PSNR/psnr_" + str(config) + "_" + str(q)
		# VQMT.exe [OriginalVideo] [ProcessedVideo] [Height] [Width] [Frames] [ChromaFormat] [Output] [Metrics]
		args=["uitvoerbare_bestanden/VQMT.exe", FilePath, DecodedVideo, "240", "416", "50", "YUV420", PSNRFile, "PSNR"]
		outFile = open('Out/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		AveragePSNR = [x for x in open(PSNRFile + "_psnr.csv", 'r').readlines() if "average" in x][0].split(',')[1]
		print "AveragePSNR = " + str(AveragePSNR)
		
		configFile = open(configPath, 'a')
		configFile.write(str(q) + "," + str(os.path.getsize(CodedVideo)) + "," + str(AveragePSNR) + '\n')
		configFile.close()

def config9():
	config = 9
	configPath = os.path.join('Opgave1', 'config'+ str(config) + '.csv')

	B = 1000000

	q = 0

	print "config_" + str(config) + ", Q = " + str(q)

	CodedVideo = "Coded/coded_" + str(config) + "_" + str(q) + ".264"
	# x264.exe -B B/1000  -v -o [output].264 --nal-hrd cbr --vbv-maxrate B/1000 --vbv-bufsize B/25000 --tune psnr --fps 25 --frames 50 --input-res 416x240 --keyint 16 --min-keyint 16 --bframe 0 --b-adapt 0 [sequentie].yuv
	args=["uitvoerbare_bestanden/x264.exe", "-B", str(B/1000), "-v", "-o", CodedVideo, "--nal-hrd", "cbr", "--vbv-maxrate",str(B/1000),"--vbv-bufsize", str(B/25000), "--tune", "psnr", "--fps", "25", "--frames", "50", "--input-res", "416x240", "--keyint", "16", "--min-keyint", "16", "--bframe", "0", "--b-adapt", "0", OriginalVideoPath]
	outFile = open('Out/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
	errFile = open('Err/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
	subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
	outFile.close()
	errFile.close()

	for q in xrange(1,11,1):
		print "config_" + str(config) + ", Q = " + str(q)

		DecodedVideo = "Decoded/decoded_" + str(config) + "_" + str(q) + ".yuv"
		# avcdecoder.exe -i [input].264 -o [output_dec].yuv
		args=["uitvoerbare_bestanden/avcdecoder.exe", "-i", CodedVideo, "-o", DecodedVideo]
		outFile = open('Out/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		PSNRFile = "PSNR/psnr_" + str(config) + "_" + str(q)
		# VQMT.exe [OriginalVideo] [ProcessedVideo] [Height] [Width] [Frames] [ChromaFormat] [Output] [Metrics]
		args=["uitvoerbare_bestanden/VQMT.exe", FilePath, DecodedVideo, "240", "416", "50", "YUV420", PSNRFile, "PSNR"]
		outFile = open('Out/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		AveragePSNR = [x for x in open(PSNRFile + "_psnr.csv", 'r').readlines() if "average" in x][0].split(',')[1]
		print "AveragePSNR = " + str(AveragePSNR)

		CodedVideo = "Coded/coded_" + str(config) + "_" + str(q) + ".264"
		# x264.exe -B B/1000  -v -o [output].264 --nal-hrd cbr --vbv-maxrate B/1000 --vbv-bufsize B/25000 --tune psnr --fps 25 --frames 50 --input-res 416x240 --keyint 16 --min-keyint 16 --bframe 0 --b-adapt 0 [sequentie].yuv
		args=["uitvoerbare_bestanden/x264.exe", "-B", str(B/1000), "-v", "-o", CodedVideo, "--nal-hrd", "cbr", "--vbv-maxrate",str(B/1000),"--vbv-bufsize", str(B/25000), "--tune", "psnr", "--fps", "25", "--frames", "50", "--input-res", "416x240", "--keyint", "16", "--min-keyint", "16", "--bframe", "0", "--b-adapt", "0", DecodedVideo]
		outFile = open('Out/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()
		
		configFile = open(configPath, 'a')
		configFile.write(str(q) + "," + str(os.path.getsize(CodedVideo)) + "," + str(AveragePSNR) + '\n')
		configFile.close()

	q = 10

	print "config_" + str(config) + ", Q = " + str(q)

	DecodedVideo = "Decoded/decoded_" + str(config) + "_" + str(q) + ".yuv"
	# avcdecoder.exe -i [input].264 -o [output_dec].yuv
	args=["uitvoerbare_bestanden/avcdecoder.exe", "-i", CodedVideo, "-o", DecodedVideo]
	outFile = open('Out/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
	errFile = open('Err/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
	subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
	outFile.close()
	errFile.close()

	PSNRFile = "PSNR/psnr_" + str(config) + "_" + str(q)
	# VQMT.exe [OriginalVideo] [ProcessedVideo] [Height] [Width] [Frames] [ChromaFormat] [Output] [Metrics]
	args=["uitvoerbare_bestanden/VQMT.exe", FilePath, DecodedVideo, "240", "416", "50", "YUV420", PSNRFile, "PSNR"]
	outFile = open('Out/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
	errFile = open('Err/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
	subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
	outFile.close()
	errFile.close()

	AveragePSNR = [x for x in open(PSNRFile + "_psnr.csv", 'r').readlines() if "average" in x][0].split(',')[1]
	print "AveragePSNR = " + str(AveragePSNR)
	configFile = open(configPath, 'a')
	configFile.write(str(q) + "," + str(os.path.getsize(CodedVideo)) + "," + str(AveragePSNR) + '\n')
	configFile.close()

def config10():
	config = 10
	configPath = os.path.join('Opgave1', 'config'+ str(config) + '.csv')

	B = 1000000

	q = 0

	CodedVideo = "Coded/coded_" + str(config) + "_" + str(q) + ".264"
	# x264.exe -B B/1000  -v -o [output].264 --nal-hrd cbr --vbv-maxrate B/1000 --vbv-bufsize B/25000 --tune psnr --fps 25 --frames 50 --input-res 416x240 --keyint 16 --min-keyint 16 --bframe 0 --b-adapt 0 [sequentie].yuv
	args=["uitvoerbare_bestanden/x264.exe", "-B", str(B/1000), "-v", "-o", CodedVideo, "--nal-hrd", "cbr", "--vbv-maxrate",str(B/1000),"--vbv-bufsize", str(B/25000), "--tune", "psnr", "--fps", "25", "--frames", "50", "--input-res", "416x240", "--keyint", "16", "--min-keyint", "16", "--bframe", "0", "--b-adapt", "0", OriginalVideoPath]
	outFile = open('Out/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
	errFile = open('Err/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
	subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
	outFile.close()
	errFile.close()

	b0 = "Decoded/decoded_" + str(config) + "_" + str(q) + ".yuv"
	# avcdecoder.exe -i [input].264 -o [output_dec].yuv
	args=["uitvoerbare_bestanden/avcdecoder.exe", "-i", CodedVideo, "-o", b0]
	outFile = open('Out/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
	errFile = open('Err/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
	subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
	outFile.close()
	errFile.close()

	PSNRFile = "PSNR/psnr_" + str(config) + "_" + str(q)
	# VQMT.exe [OriginalVideo] [ProcessedVideo] [Height] [Width] [Frames] [ChromaFormat] [Output] [Metrics]
	args=["uitvoerbare_bestanden/VQMT.exe", FilePath, b0, "240", "416", "50", "YUV420", PSNRFile, "PSNR"]
	outFile = open('Out/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
	errFile = open('Err/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
	subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
	outFile.close()
	errFile.close()

	AveragePSNR = [x for x in open(PSNRFile + "_psnr.csv", 'r').readlines() if "average" in x][0].split(',')[1]
	print "AveragePSNR = " + str(AveragePSNR)
	configFile = open(configPath, 'a')
	configFile.write(str(q) + "," + str(os.path.getsize(CodedVideo)) + "," + str(AveragePSNR) + '\n')
	configFile.close()

	for q in [1500000, 2000000, 4000000, 10000000]:
		print "config_" + str(config) + ", Q = " + str(q)

		CodedVideo = "Coded/coded_" + str(config) + "_" + str(q) + ".264"
		# x264.exe -B B/1000  -v -o [output].264 --nal-hrd cbr --vbv-maxrate B/1000 --vbv-bufsize B/25000 --tune psnr --fps 25 --frames 50 --input-res 416x240 --keyint 16 --min-keyint 16 --bframe 0 --b-adapt 0 [sequentie].yuv
		args=["uitvoerbare_bestanden/x264.exe", "-B", str(q/1000), "-v", "-o", CodedVideo, "--nal-hrd", "cbr", "--vbv-maxrate",str(q/1000),"--vbv-bufsize", str(q/25000), "--tune", "psnr", "--fps", "25", "--frames", "50", "--input-res", "416x240", "--keyint", "16", "--min-keyint", "16", "--bframe", "0", "--b-adapt", "0", b0]
		outFile = open('Out/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/coded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		DecodedVideo = "Decoded/decoded_" + str(config) + "_" + str(q) + ".yuv"
		# avcdecoder.exe -i [input].264 -o [output_dec].yuv
		args=["uitvoerbare_bestanden/avcdecoder.exe", "-i", CodedVideo, "-o", DecodedVideo]
		outFile = open('Out/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/decoded_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		PSNRFile = "PSNR/psnr_" + str(config) + "_" + str(q)
		# VQMT.exe [OriginalVideo] [ProcessedVideo] [Height] [Width] [Frames] [ChromaFormat] [Output] [Metrics]
		args=["uitvoerbare_bestanden/VQMT.exe", FilePath, DecodedVideo, "240", "416", "50", "YUV420", PSNRFile, "PSNR"]
		outFile = open('Out/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		errFile = open('Err/psnr_' + str(config) + "_" + str(q) + '.txt', 'w')
		subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
		outFile.close()
		errFile.close()

		AveragePSNR = [x for x in open(PSNRFile + "_psnr.csv", 'r').readlines() if "average" in x][0].split(',')[1]
		print "AveragePSNR = " + str(AveragePSNR)
		configFile = open(configPath, 'a')
		configFile.write(str(q) + "," + str(os.path.getsize(CodedVideo)) + "," + str(AveragePSNR) + '\n')
		configFile.close()

#config1()
#config2()
#config3()
#config4()
#config5()
#config6()
#config7()
#config8()
#config9()
#config10()
