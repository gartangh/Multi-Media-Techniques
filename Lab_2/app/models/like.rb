class Like < ActiveRecord::Base
	belongs_to :video
	belongs_to :user

	validates_uniqueness_of :user_id, scope: :video_id
end
