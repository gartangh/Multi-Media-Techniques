import os
import subprocess

def config1():
	config = 1

	for video in ["PartyScene", "RaceHorses", "Vidyo"]:

		extention = "_416x240_25fps.yuv"
		OriginalVideo = video + extention
		# Open bestand
		OriginalVideoPath = os.path.join('YUV-bestanden', OriginalVideo)
		# Bestandsgrootte
		FileSize = os.path.getsize(OriginalVideoPath)
		print "Filesize = " + str(FileSize)
	
		configPath = os.path.join('Opgave2', 'config'+ str(config) + '.csv')

		for q in xrange(1,52,5):
			# x264
			print "config_" + str(config) + ", Q = " + str(q) + "_264"

			CodedVideo = "Coded/coded_" + video + "_" + str(config) + "_" + str(q) + "_264.264"
			# x264.exe -q [quantisatieparameter] -v -o [output].264 --tune psnr --fps 25 --frames 50 --input-res 416x240  --keyint 16 --min-keyint 16 --bframe 4 --b-adapt 0 --me dia --subme 4 [sequentie].yuv
			args=["uitvoerbare_bestanden/x264.exe", "-q", str(q), "-v", "-o", CodedVideo, "--tune", "psnr", "--fps", "25", "--frames", "50", "--input-res", "416x240", "--keyint", "16", "--min-keyint", "16", "--bframe", "4", "--b-adapt", "0", "--me", "dia", "--subme", "4", OriginalVideoPath]
			outFile = open('Out/' + video + "_" + str(config) + "_" + str(q) + '_264.txt', 'w')
			errFile = open('Err/' + video + "_" + str(config) + "_" + str(q) + '_264.txt', 'w')
			subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
			outFile.close()
			errFile.close()

			DecodedVideo = "Decoded/decoded_" + video + "_" + str(config) + "_" + str(q) + "_264.yuv"
			# avcdecoder.exe -i [input].264 -o [output_dec].yuv
			args=["uitvoerbare_bestanden/AVCDecoder.exe", "-i", CodedVideo, "-o", DecodedVideo]
			outFile = open('Out/' + video + "_" + str(config) + "_" + str(q) + '_264.txt', 'w')
			errFile = open('Err/' + video + "_" + str(config) + "_" + str(q) + '_264.txt', 'w')
			subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
			outFile.close()
			errFile.close()

			PSNRFile = "PSNR/" + video + "_" + str(config) + "_" + str(q) + "_264"
			# VQMT.exe [OriginalVideo] [ProcessedVideo] [Height] [Width] [Frames] [ChromaFormat] [Output] [Metrics]
			args=["uitvoerbare_bestanden/VQMT.exe", OriginalVideoPath, DecodedVideo, "240", "416", "50", "YUV420", PSNRFile, "PSNR"]
			outFile = open('Out/' + video + "_" + str(config) + "_" + str(q) + '_264.txt', 'w')
			errFile = open('Err/' + video + "_" + str(config) + "_" + str(q) + '_264.txt', 'w')
			subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
			outFile.close()
			errFile.close()

			AveragePSNR = [x for x in open(PSNRFile + "_psnr.csv", 'r').readlines() if "average" in x][0].split(',')[1]
			print "AveragePSNR = " + str(AveragePSNR)
			
			configFile = open(configPath, 'a')
			configFile.write(str(q) + "," + str(os.path.getsize(CodedVideo)) + "," +  str(AveragePSNR) + '\n')
			configFile.close()

			# x265
			print "config_" + str(config) + ", Q = " + str(q) + "_265"

			CodedVideo = "Coded/coded_" + video + "_" + str(config) + "_" + str(q) + "_265.265"
			# x265.exe -q [quantisatieparameter] -v -o [output].264 --tune psnr --fps 25 --frames 50 --input-res 416x240  --keyint 16 --min-keyint 16 --bframe 4 --b-adapt 0 --me dia --subme 4 --preset veryslow [sequentie].yuv
			args=["uitvoerbare_bestanden/x265.exe", "-q", str(q), "-o", CodedVideo,  "--tune", "psnr", "--fps", "25", "--frames", "50", "--input-res", "416x240", "--keyint", "16", "--min-keyint", "16", "--bframe", "4", "--b-adapt", "0", "--me", "dia", "--preset", "veryslow", "--input", OriginalVideoPath]
			outFile = open('Out/' + video + "_" + str(config) + "_" + str(q) + '_265.txt', 'w')
			errFile = open('Err/' + video + "_" + str(config) + "_" + str(q) + '_265.txt', 'w')
			subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
			outFile.close()
			errFile.close()

			DecodedVideo = "Decoded/decoded_" + video + "_" + str(config) + "_" + str(q) + "_265.yuv"
			# hevcdecoder.exe -b [input].264 -o [output_dec].yuv
			args=["uitvoerbare_bestanden/HEVCDecoder.exe", "-b", CodedVideo, "-o", DecodedVideo]
			outFile = open('Out/' + video + "_" + str(config) + "_" + str(q) + '_265.txt', 'w')
			errFile = open('Err/' + video + "_" + str(config) + "_" + str(q) + '_265.txt', 'w')
			subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
			outFile.close()
			errFile.close()

			PSNRFile = "PSNR/" + video + "_" + str(config) + "_" + str(q) + "_265"
			# VQMT.exe [OriginalVideo] [ProcessedVideo] [Height] [Width] [Frames] [ChromaFormat] [Output] [Metrics]
			args=["uitvoerbare_bestanden/VQMT.exe", OriginalVideoPath, DecodedVideo, "240", "416", "50", "YUV420", PSNRFile, "PSNR"]
			outFile = open('Out/' + video + "_" + str(config) + "_" + str(q) + '_265.txt', 'w')
			errFile = open('Err/' + video + "_" + str(config) + "_" + str(q) + '_265.txt', 'w')
			subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
			outFile.close()
			errFile.close()

			AveragePSNR = [x for x in open(PSNRFile + "_psnr.csv", 'r').readlines() if "average" in x][0].split(',')[1]
			print "AveragePSNR = " + str(AveragePSNR)
			
			configFile = open(configPath, 'a')
			configFile.write(str(q) + "," + str(os.path.getsize(CodedVideo)) + "," +  str(AveragePSNR) + '\n')
			configFile.close()

def config2():
	config = 2

	for video in ["PartyScene", "RaceHorses", "Vidyo"]:

		extention = "_416x240_25fps.yuv"
		OriginalVideo = video + extention
		# Open bestand
		OriginalVideoPath = os.path.join('YUV-bestanden', OriginalVideo)
		# Bestandsgrootte
		FileSize = os.path.getsize(OriginalVideoPath)
		print "Filesize = " + str(FileSize)
	
		configPath = os.path.join('Opgave2', 'config'+ str(config) + '.csv')

		for q in xrange(1,52,5):
			# x264
			print "config_" + str(config) + ", Q = " + str(q) + "_264"

			CodedVideo = "Coded/coded_" + video + "_" + str(config) + "_" + str(q) + "_264.264"
			# x264.exe -q [quantisatieparameter] -v -o [output].264 --tune psnr --fps 25 --frames 50 --input-res 416x240  --keyint 16 --min-keyint 16 --bframe 4 --b-adapt 0 --me dia --subme 4 [sequentie].yuv
			args=["uitvoerbare_bestanden/x264.exe", "-q", str(q), "-v", "-o", CodedVideo, "--tune", "psnr", "--fps", "25", "--frames", "50", "--input-res", "416x240", "--keyint", "16", "--min-keyint", "16", "--bframe", "4", "--b-adapt", "0", "--me", "dia", "--subme", "4", OriginalVideoPath]
			outFile = open('Out/' + video + "_" + str(config) + "_" + str(q) + '_264.txt', 'w')
			errFile = open('Err/' + video + "_" + str(config) + "_" + str(q) + '_264.txt', 'w')
			subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
			outFile.close()
			errFile.close()

			DecodedVideo = "Decoded/decoded_" + video + "_" + str(config) + "_" + str(q) + "_264.yuv"
			# avcdecoder.exe -i [input].264 -o [output_dec].yuv
			args=["uitvoerbare_bestanden/AVCDecoder.exe", "-i", CodedVideo, "-o", DecodedVideo]
			outFile = open('Out/' + video + "_" + str(config) + "_" + str(q) + '_264.txt', 'w')
			errFile = open('Err/' + video + "_" + str(config) + "_" + str(q) + '_264.txt', 'w')
			subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
			outFile.close()
			errFile.close()

			PSNRFile = "PSNR/" + video + "_" + str(config) + "_" + str(q) + "_264"
			# VQMT.exe [OriginalVideo] [ProcessedVideo] [Height] [Width] [Frames] [ChromaFormat] [Output] [Metrics]
			args=["uitvoerbare_bestanden/VQMT.exe", OriginalVideoPath, DecodedVideo, "240", "416", "50", "YUV420", PSNRFile, "PSNR"]
			outFile = open('Out/' + video + "_" + str(config) + "_" + str(q) + '_264.txt', 'w')
			errFile = open('Err/' + video + "_" + str(config) + "_" + str(q) + '_264.txt', 'w')
			subprocess.Popen(args, stdout=outFile, stderr=errFile).communicate()[0]
			outFile.close()
			errFile.close()

			AveragePSNR = [x for x in open(PSNRFile + "_psnr.csv", 'r').readlines() if "average" in x][0].split(',')[1]
			print "AveragePSNR = " + str(AveragePSNR)
			
			configFile = open(configPath, 'a')
			configFile.write(str(q) + "," + str(os.path.getsize(CodedVideo)) + "," +  str(AveragePSNR) + '\n')
			configFile.close()


#config1()
config2()