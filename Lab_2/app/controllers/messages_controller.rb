class MessagesController < ApplicationController
	def new
		@message = Message.new
	end

	def create
		params[:message][:date] = DateTime.current
		
		@video = Video.find(params[:video_id])
		@message = @video.messages.create(params[:message].permit(:user_id, :date, :text))
		
		redirect_to video_path(@video)
	end

	def edit
		@video = Video.find(params[:video_id])
		@message = Message.find(params[:id])
	end

	def update
		@video = Video.find(params[:video_id])
		@message = Message.find(params[:id])
		params[:message][:date] = DateTime.current
    	if @message.update(params[:message].permit(:user_id, :date, :text))
			redirect_to video_path(@video)
		else
			render 'edit'
		end
	end

	def destroy
		@video = Video.find(params[:video_id])
		@message = @video.messages.find(params[:id])
		@message.destroy

		redirect_to video_path(@video)
	end
end