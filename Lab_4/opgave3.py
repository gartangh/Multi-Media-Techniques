import os
import subprocess

OriginalVideo = "BasketballDrive_1280x720_25fps.yuv"

FullVideoSize = 243 000 000 000 # byte (243 GB)

# Open bestand
OriginalFilePath = os.path.join('YUV-bestanden', OriginalVideo)
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

config1()