class UsersController < ApplicationController
	def index
		@users = User.all
	end

	def new
		@user = User.new
	end

	def create
		@user = User.new(user_params)
		
		if @user.save
			redirect_to @user
		else
			render 'new'
		end
	end

	def show
		if valid_user?
			@user = User.find(params[:id])
		else
			render file: "pages/404.html.erb", status: :not_found
		end
	end

	def edit
		@user = User.find(params[:id])
	end

	def update
		@user = User.find(params[:id])
		
		if @user.update(user_params)
			redirect_to @user
		else
			render 'edit'
		end
	end

	def destroy
		@user = User.find(params[:id])
		@user.destroy
		
		redirect_to users_path
	end

	private
	def user_params
		params.require(:user).permit(:name, :birthdate, :email)
	end

	def valid_user?
		User.exists?(id: params[:id])
	end
end