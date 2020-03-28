class CreateMessages < ActiveRecord::Migration
	def change
		create_table :messages do |t|
			t.references :video, index: true
			t.references :user, index: true
			
			t.datetime :date
			t.text :text
		end
	end
end