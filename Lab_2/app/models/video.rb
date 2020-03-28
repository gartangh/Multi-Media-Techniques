class Video < ActiveRecord::Base
	has_many :messages, dependent: :destroy
	has_many :users, :through => :messages
	has_many :likes, dependent: :destroy
	
	validates :title, presence: true, length: { minimum: 2 }
	validates :url, presence: true
	validates :description, presence: true, length: { minimum: 2 }
end