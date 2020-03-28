class VideosController < ApplicationController
	def index
		@videos = Video.all
	end

	def new
		@video = Video.new
	end

	def create
		@video = Video.new(video_params)
		
		if @video.save
			redirect_to @video
		else
			render 'new'
		end
	end

	def show
		if valid_video?
			@video = Video.find(params[:id])
		else
			render file: "pages/404.html.erb", status: :not_found
		end
	end

	def edit
		@video = Video.find(params[:id])
	end

	def update
		@video = Video.find(params[:id])
		
		if @video.update(video_params)
			redirect_to @video
		else
			render 'edit'
		end
	end

	def destroy
		@video = Video.find(params[:id])
		@video.destroy
		
		redirect_to videos_path
	end

	private
	def video_params
		params.require(:video).permit(:title, :url, :description)
	end

	def valid_video?
		Video.exists?(id: params[:id])
	end
end