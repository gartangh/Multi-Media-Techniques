class Message < ActiveRecord::Base
	belongs_to :user
	belongs_to :video
	
	validates :text, presence: true, length: { minimum: 1 }
	validates :date, presence: true
end