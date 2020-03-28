class User < ActiveRecord::Base
	has_many :messages, dependent: :destroy
	has_many :videos, :through => :messages
	has_many :likes, dependent: :destroy
	
	validates :email, presence: true, length: { minimum: 6 }
	validates :name , presence: true, length: { minimum: 2 }
	validates :birthdate, presence: true
end