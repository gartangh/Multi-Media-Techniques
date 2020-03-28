class LikesController < ApplicationController
	def new
		@like = Like.new
	end

	def create
		@video = Video.find(params[:video_id])
		@like = @video.likes.create(params[:message].permit(:user_id))
		
		redirect_to video_path(@video)
	end

	def destroy
		@video = Video.find(params[:video_id])
		@like = @video.likes.find(params[:id])
		@like.destroy

		redirect_to video_path(@video)
	end
end
